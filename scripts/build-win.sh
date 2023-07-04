#!/bin/bash
set -e

rm -rf /src/tmp
git config --global advice.detachedHead false
git clone $GIT_REPOSITORY /src/tmp/source --depth 1 --branch $VERSION

vs_cmd "cmd /c /repo/scripts/build-win.bat"

# cmake /tmp/source -B /tmp/build-debug \
#     -DCMAKE_INSTALL_PREFIX=/tmp/install-debug \
#     -DCMAKE_TOOLCHAIN_FILE=$TOOLCHAIN_FILE \
#     -DCMAKE_BUILD_TYPE=Debug .. \
#     -DCMAKE_C_COMPILER=$CC \
#     -DCMAKE_CXX_COMPILER=$CXX \
#     -DBUILD_SHARED_LIBS=OFF \
#     -DGLFW_BUILD_EXAMPLES=OFF \
#     -DGLFW_BUILD_TESTS=OFF \
#     -DGLFW_BUILD_DOCS=OFF

# cmake /tmp/source -B /tmp/build-release \
#     -DCMAKE_INSTALL_PREFIX=/tmp/install-release \
#     -DCMAKE_TOOLCHAIN_FILE=$TOOLCHAIN_FILE \
#     -DCMAKE_BUILD_TYPE=Release .. \
#     -DCMAKE_C_COMPILER=$CC \
#     -DCMAKE_CXX_COMPILER=$CXX \
#     -DBUILD_SHARED_LIBS=OFF \
#     -DGLFW_BUILD_EXAMPLES=OFF \
#     -DGLFW_BUILD_TESTS=OFF \
#     -DGLFW_BUILD_DOCS=OFF

# cmake --build /tmp/build-debug -j $(nproc)
# cmake --build /tmp/build-debug --target install
# cmake --build /tmp/build-release -j $(nproc)
# cmake --build /tmp/build-release --target install

mkdir -p /tmp/archive/debug/lib /tmp/archive/release/lib
cp /package/cmake/CMakeLists.txt /tmp/archive/
cp /tmp/install-debug/lib/libglfw3.a /tmp/archive/debug/lib/
cp /tmp/install-release/lib/libglfw3.a /tmp/archive/release/lib/
cp -r /tmp/install-debug/include /tmp/archive/debug
cp -r /tmp/install-release/include /tmp/archive/release

mkdir -p /package/out
cd /tmp/archive && tar -zcvf /package/out/$PACKAGE.tar.gz **


git --version
