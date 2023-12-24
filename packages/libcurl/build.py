from scripts.tools import LibraryBuilder
import os

class Builder(LibraryBuilder):
    name = "libcurl"
    version = "8.5.0"

    def source(self):
        self.source_git_repo("https://github.com/curl/curl.git", "curl-8_5_0")

    def patch_sources(self):
        self.remove_file(file = os.path.join(self.source_dir, "CMake", "FindMbedTLS.cmake"))
        self.replace_in_file(
            file = os.path.join(self.source_dir, "CMakeLists.txt"),
            find = "${MBEDTLS_LIBRARIES}",
            replace = "MbedTLS::mbedtls"
        )

    def depends(self):
        self.pull_of_dependency("mbedtls", "3.4.0")

    def build(self):
        self.build_generic_cmake_project(
            [
                "-DBUILD_SHARED_LIBS=OFF", 
                "-DBUILD_CURL_EXE=OFF",
                "-DENABLE_UNICODE=ON",
                "-DCURL_USE_MBEDTLS=ON",
                f'-DCMAKE_PREFIX_PATH="{self.get_dependency_dir("mbedtls")}"',
            ]
        )
        
    def package(self):
        self.archive_generic_package()
