import os
import sys
import shutil

def get_root_dir():
    return os.getcwd()

def get_working_dir(package_name):
    return os.sep.join([get_root_dir(), 'temp', package_name])

def get_source_dir(package_name):
    return os.sep.join([get_working_dir(package_name), 'source'])

def get_debug_build_dir(package_name):
    return os.sep.join([get_working_dir(package_name), 'build_debug'])

def get_release_build_dir(package_name):
    return os.sep.join([get_working_dir(package_name), 'build_release'])

def get_debug_install_dir(package_name):
    return os.sep.join([get_working_dir(package_name), 'install_debug'])

def get_release_install_dir(package_name):
    return os.sep.join([get_working_dir(package_name), 'install_release'])

def get_archive_dir(package_name):
    return os.sep.join([get_working_dir(package_name), 'archive'])

def get_output_dir():
    return os.sep.join([get_root_dir(), 'out'])

def cmd(command):
    if os.system(command) != 0:
        raise Exception(f'Failed to execute command: {command}')

def replace_in_file(file, find, replace):
    with open(file, 'r') as f:
        content = f.read()
    content = content.replace(find, replace)
    with open(file, 'w') as f:
        f.write(content)

def remove_file(file):
    os.remove(file)

def insert_before_file(file, insert):
    with open(file, 'r') as f:
        content = f.read()
    content = insert + content
    with open(file, 'w') as f:
        f.write(content)

def clone_git_repository(git_repository, git_tag, package_name):
    sourcedir = get_source_dir(package_name)

    cmd('git config --global advice.detachedHead false')
    cmd(f'git clone {git_repository} {sourcedir} --depth=1 --single-branch --branch={git_tag}')

def install_build_requirements(extra_unix_dependencies = []):
    if (os.environ['CXX_COMPILER'] != 'msvc'):
        extra_unix_dependencies += os.environ['CC_COMPILER_PACKAGE']

    if (os.environ['CXX_COMPILER'] != 'msvc'):
        extra_unix_dependencies += os.environ['CXX_COMPILER_PACKAGE']
    
    deps = ' '.join(extra_unix_dependencies)
    cmd(f'apt-get update && apt-get install -y {deps}')

def build_generic_cmake_project(package_name, cmake_args = [], cmake_module_paths = [], cmake_module_path_root = '', cmake_args_debug = [], cmake_args_release = []):
    if (os.environ['CXX_COMPILER'] != 'msvc'):
        cmake_args.append(f'-DCMAKE_C_COMPILER={os.environ["CC_COMPILER"]}')
    
    if (os.environ['CXX_COMPILER'] != 'msvc'):
        cmake_args.append(f'-DCMAKE_CXX_COMPILER={os.environ["CXX_COMPILER"]}')
    
    if (os.environ["TOOLCHAIN_FILE"] != ''):
        cmake_args.append(f'-DCMAKE_TOOLCHAIN_FILE={os.environ["TOOLCHAIN_FILE"]}')

    cmake_args.append(f'-DBUILD_SHARED_LIBS=OFF')
    cmake_args.append(f'-DPython_ROOT_DIR={os.path.dirname(sys.executable)}')
    cmake_args.append(f'-DPython3_ROOT_DIR={os.path.dirname(sys.executable)}')

    if cmake_module_paths != []:
        cmake_args.append(f'-DCMAKE_MODULE_PATH={";".join(cmake_module_paths)}')

    os.makedirs(get_debug_build_dir(package_name), exist_ok=True)
    os.makedirs(get_release_build_dir(package_name), exist_ok=True)

    args_debug = []
    args_debug.append(f'{get_source_dir(package_name)}')
    args_debug.append(f'-B {get_debug_build_dir(package_name)}')
    args_debug.append(f'-DCMAKE_BUILD_TYPE=Debug')
    args_debug.append(f'-DCMAKE_INSTALL_PREFIX={get_debug_install_dir(package_name)}')
    args_debug.append(' '.join(cmake_args))
    args_debug.append(' '.join(cmake_args_debug))

    args_release = []
    args_release.append(f'{get_source_dir(package_name)}')
    args_release.append(f'-B {get_release_build_dir(package_name)}')
    args_release.append(f'-DCMAKE_BUILD_TYPE=Release')
    args_release.append(f'-DCMAKE_INSTALL_PREFIX={get_release_install_dir(package_name)}')
    args_release.append(' '.join(cmake_args))
    args_release.append(' '.join(cmake_args_release))

    cmd(f'cmake -G Ninja {" ".join(args_debug)}')
    cmd(f'cmake --build {get_debug_build_dir(package_name)} --config Debug { "-j $(nproc)}" if os.environ["CXX_COMPILER"] != "msvc" else "" }')
    cmd(f'cmake --build {get_debug_build_dir(package_name)} --target install')

    cmd(f'cmake -G Ninja {" ".join(args_release)}')
    cmd(f'cmake --build {get_release_build_dir(package_name)} --config Release { "-j $(nproc)}" if os.environ["CXX_COMPILER"] != "msvc" else "" }')
    cmd(f'cmake --build {get_release_build_dir(package_name)} --target install')

def archive_generic_package(package_name, files):
    os.makedirs(get_archive_dir(package_name), exist_ok=True)
    os.makedirs(get_output_dir(), exist_ok=True)

    for file in files:
        sourcefile = ''
        targetfile = ''

        if (len(file) == 2):
            sourcefile = file[0]
            targetfile = os.sep.join([get_archive_dir(package_name), file[1]])
        else:
            sourcefile = os.sep.join([file[0], file[1]])
            targetfile = os.sep.join([get_archive_dir(package_name), file[2]])

        if os.path.isdir(sourcefile):
            shutil.copytree(sourcefile, targetfile, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(targetfile), exist_ok=True)
            shutil.copy(sourcefile, targetfile)

    cmd(f'cd {get_archive_dir(package_name)} && tar -zcvf {get_output_dir()}/{os.environ["FULL_PACKAGE_NAME"]}.tar.gz *')

def clear_temp_folder():
    if os.path.exists(os.sep.join([get_root_dir(), 'temp'])):
        shutil.rmtree(os.sep.join([get_root_dir(), 'temp']))