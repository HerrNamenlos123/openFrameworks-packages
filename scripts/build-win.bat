@echo off

cmake --version

nmake --version
cmake -G "Visual Studio 15 2017" -A x64 Z:/src/tmp/source -B Z:/src/tmp/build-debug^
    -DCMAKE_INSTALL_PREFIX=Z:/src/tmp/install-debug^
    -DCMAKE_TOOLCHAIN_FILE=$TOOLCHAIN_FILE^
    -DCMAKE_BUILD_TYPE=Debug^
    -DCMAKE_C_COMPILER=$CC^
    -DCMAKE_CXX_COMPILER=$CXX^
    -DBUILD_SHARED_LIBS=OFF^
    -DGLFW_BUILD_EXAMPLES=OFF^
    -DGLFW_BUILD_TESTS=OFF^
    -DGLFW_BUILD_DOCS=OFF

cmake -G "Visual Studio 15 2017" -A x64 Z:/src/tmp/source -B Z:/src/tmp/build-release^
    -DCMAKE_INSTALL_PREFIX=Z:/src/tmp/install-release^
    -DCMAKE_TOOLCHAIN_FILE=$TOOLCHAIN_FILE^
    -DCMAKE_BUILD_TYPE=Release^
    -DCMAKE_C_COMPILER=$CC^
    -DCMAKE_CXX_COMPILER=$CXX^
    -DBUILD_SHARED_LIBS=OFF^
    -DGLFW_BUILD_EXAMPLES=OFF^
    -DGLFW_BUILD_TESTS=OFF^
    -DGLFW_BUILD_DOCS=OFF

cmake --build Z:/src/tmp/build-debug -j $(nproc)
cmake --build Z:/src/tmp/build-debug --target install
cmake --build Z:/src/tmp/build-release -j $(nproc)
cmake --build Z:/src/tmp/build-release --target install