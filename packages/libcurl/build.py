from scripts import tools

tools.clone_git_repository(git_repository = "https://github.com/Mbed-TLS/mbedtls.git",
                           git_tag = "v3.4.0",
                           working_dir = "mbedtls")

tools.build_generic_cmake_project(working_dir = "mbedtls",
                                  cmake_args = ["-DENABLE_TESTING=OFF",
                                                "-DENABLE_PROGRAMS=OFF",
                                                "-DBUILD_SHARED_LIBS=OFF",
                                                "-DGEN_FILES=ON"])

tools.clone_git_repository(git_repository = "https://github.com/curl/curl.git",
                           git_tag = "curl-8_1_2")

tools.remove_file(file = tools.WORKING_DIR + tools.SOURCE_DIR + "/CMake/FindMbedTLS.cmake") # Forcefully remove curl's FindMbedTLS.cmake to make it find ours instead

tools.cmd("tree mbedtls")

tools.build_generic_cmake_project(cmake_args = ["-DBUILD_SHARED_LIBS=OFF", 
                                                "-DBUILD_CURL_EXE=OFF",
                                                "-DENABLE_UNICODE=ON",
                                                "-DCURL_USE_MBEDTLS=ON"],
                                  cmake_args_debug = [f'-DMbedTLS_DIR=mbedtls{tools.INSTALL_DIR_DEBUG}/lib/cmake/MbedTLS'],
                                  cmake_args_release = [f'-DMbedTLS_DIR=mbedtls{tools.INSTALL_DIR_RELEASE}/lib/cmake/MbedTLS'])

tools.archive_generic_package(files = [
    [tools.SOURCE_DIR + "/include/openssl", "include/openssl"],
    [tools.SOURCE_DIR + "/include/crypto", "include/crypto"],
    [tools.INSTALL_DIR_DEBUG + f"/lib64/{tools.release_lib_name('crypto')}", f"lib-debug/{tools.release_lib_name('crypto')}"],
    [tools.INSTALL_DIR_DEBUG + f"/lib64/{tools.release_lib_name('ssl')}", f"lib-debug/{tools.release_lib_name('ssl')}"],
    [tools.INSTALL_DIR_RELEASE + f"/lib64/{tools.release_lib_name('crypto')}", f"lib-release/{tools.release_lib_name('crypto')}"],
    [tools.INSTALL_DIR_RELEASE + f"/lib64/{tools.release_lib_name('ssl')}", f"lib-release/{tools.release_lib_name('ssl')}"],
])