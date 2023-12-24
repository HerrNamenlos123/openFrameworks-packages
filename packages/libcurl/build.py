from scripts import tools
import os

# Initialize the build environment
tools.init()

# Build MbedTLS
tools.clone_git_repository("mbedtls", "https://github.com/Mbed-TLS/mbedtls.git", "v3.4.0")
tools.append_to_file( # Inject a "-d" postfix to allow combined debug/release builds
    file = os.path.join([tools.get_source_dir('mbedtls'), "library", "CMakeLists.txt"]), 
    append = "if(NOT DEFINED CMAKE_DEBUG_POSTFIX)\nset(CMAKE_DEBUG_POSTFIX \"-d\")\nendif()\n\n"
)
tools.build_generic_cmake_project("mbedtls", ["-DENABLE_TESTING=OFF", "-DENABLE_PROGRAMS=OFF", "-DGEN_FILES=ON"])

# Build libcurl
tools.clone_git_repository("libcurl", "https://github.com/curl/curl.git", "curl-8_1_2")
# Forcefully remove curl's FindMbedTLS.cmake to make it find ours instead
tools.remove_file(file = os.path.join([tools.get_source_dir('libcurl'), "/CMake/FindMbedTLS.cmake"]))
tools.replace_in_file(
    file = os.path.join([tools.get_source_dir('libcurl'), "/CMakeLists.txt"]),
    find = "${MBEDTLS_LIBRARIES}",      # Patch it to find our MbedTLS
    replace = "MbedTLS::mbedtls"
)

tools.build_generic_cmake_project(
    package_name = "libcurl",
    cmake_args = [
        f'-DMbedTLS_DIR="{os.path.join([tools.get_install_dir("mbedtls"), "lib", "cmake", "MbedTLS"])}"',
        "-DBUILD_SHARED_LIBS=OFF", 
        "-DBUILD_CURL_EXE=OFF",
        "-DENABLE_UNICODE=ON",
        "-DCURL_USE_MBEDTLS=ON"
    ]
)

tools.archive_generic_package(package_name = 'libcurl', files = [
    [tools.get_install_dir('mbedtls'), "."],
    [tools.get_install_dir('libcurl'), "."],
])
