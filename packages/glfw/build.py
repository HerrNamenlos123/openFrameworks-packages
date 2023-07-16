from scripts import tools
import os

tools.install_build_requirements(
    extra_unix_dependencies = [
        'xorg-dev',
    ]
)

tools.build_generic_cmake_project(git_repository = "https://github.com/glfw/glfw", 
                                  git_tag = "3.3.8", 
                                  cmake_args = ["-DGLFW_BUILD_EXAMPLES=OFF", 
                                                "-DGLFW_BUILD_TESTS=OFF", 
                                                "-DGLFW_BUILD_DOCS=OFF",
                                                "-DGLFW_BUILD_X11=OFF"]
)

tools.archive_generic_package(package_name = 'glfw', output_library_name = 'glfw3')