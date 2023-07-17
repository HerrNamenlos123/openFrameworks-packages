from scripts import tools
import os

tools.clear_temp_folder()
tools.clone_git_repository(package_name = "mbedtls",
                           git_repository = "https://github.com/Mbed-TLS/mbedtls.git",
                           git_tag = "v3.4.0")

tools.build_generic_cmake_project(package_name = "mbedtls",
                                  cmake_args = ["-DENABLE_TESTING=OFF",
                                                "-DENABLE_PROGRAMS=OFF",
                                                "-DGEN_FILES=ON"])

tools.clone_git_repository(package_name = "libcurl",
                           git_repository = "https://github.com/curl/curl.git",
                           git_tag = "curl-8_1_2")

# Forcefully remove curl's FindMbedTLS.cmake to make it find ours instead
tools.remove_file(file = os.sep.join([tools.get_source_dir('libcurl'), "/CMake/FindMbedTLS.cmake"]))

tools.replace_in_file(file = os.sep.join([tools.get_source_dir('libcurl'), "/CMakeLists.txt"]),
                      find = "${MBEDTLS_LIBRARIES}", replace = "MbedTLS::mbedtls")  # Use our modern targets instead of legacy approach

tools.build_generic_cmake_project(
    package_name = "libcurl",
    cmake_args_debug = [
        f'-DMbedTLS_DIR="{os.sep.join([tools.get_debug_install_dir("mbedtls"), "lib", "cmake", "MbedTLS"])}"'
    ],
    cmake_args_release = [
        f'-DMbedTLS_DIR="{os.sep.join([tools.get_release_install_dir("mbedtls"), "lib", "cmake", "MbedTLS"])}"'
    ],
    cmake_args = [
        "-DBUILD_SHARED_LIBS=OFF", 
        "-DBUILD_CURL_EXE=OFF",
        "-DENABLE_UNICODE=ON",
        "-DCURL_USE_MBEDTLS=ON"
    ]
)

tools.archive_generic_package(package_name = 'libcurl', files = [
    [tools.get_debug_install_dir('mbedtls'), "debug"],
    [tools.get_release_install_dir('mbedtls'), "release"],
    [tools.get_debug_install_dir('libcurl'), "debug"],
    [tools.get_release_install_dir('libcurl'), "release"],
])