from scripts import tools
import os

# tools.clone_git_repository(git_repository = "https://github.com/Mbed-TLS/mbedtls.git",
#                            git_tag = "v3.4.0",
#                            working_dir = "mbedtls")

# tools.build_generic_cmake_project(working_dir = "mbedtls",
#                                   cmake_args = ["-DENABLE_TESTING=OFF",
#                                                 "-DENABLE_PROGRAMS=OFF",
#                                                 "-DBUILD_SHARED_LIBS=OFF",
#                                                 "-DGEN_FILES=ON"])

# tools.clone_git_repository(git_repository = "https://github.com/curl/curl.git",
#                            git_tag = "curl-8_1_2")

# tools.remove_file(file = tools.WORKING_DIR + tools.SOURCE_DIR + "/CMake/FindMbedTLS.cmake") # Forcefully remove curl's FindMbedTLS.cmake to make it find ours instead

# tools.replace_in_file(file = tools.WORKING_DIR + tools.SOURCE_DIR + "/CMakeLists.txt",
#                       find = "${MBEDTLS_LIBRARIES}", replace = "MbedTLS::mbedtls")  # Use our targets

# tools.build_generic_cmake_project(cmake_args = ["-DBUILD_SHARED_LIBS=OFF", 
#                                                 "-DBUILD_CURL_EXE=OFF",
#                                                 "-DENABLE_UNICODE=ON",
#                                                 "-DCURL_USE_MBEDTLS=ON"],
#                                   cmake_args_debug = [f'-DMbedTLS_DIR="{os.getcwd()}/mbedtls{tools.INSTALL_DIR_DEBUG}/lib/cmake/MbedTLS"'],
#                                   cmake_args_release = [f'-DMbedTLS_DIR="{os.getcwd()}/mbedtls{tools.INSTALL_DIR_RELEASE}/lib/cmake/MbedTLS"'])

tools.archive_generic_package(files = [
    [tools.WORKING_DIR + tools.INSTALL_DIR_DEBUG + "/include", "include"],
    [tools.WORKING_DIR + tools.INSTALL_DIR_DEBUG + "/lib", "lib"],
    [tools.WORKING_DIR + tools.INSTALL_DIR_RELEASE + "/lib", "lib"]
])