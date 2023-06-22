FROM debian:10

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc-7 g++-7 make cmake git
RUN apt-get install -y libx11-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev

RUN git config --global advice.detachedHead false
RUN git clone https://github.com/glfw/glfw.git
WORKDIR /glfw
RUN git checkout 3.3.8

RUN mkdir build
WORKDIR /glfw/build

RUN cmake -DCMAKE_BUILD_TYPE=Release .. \
    -DBUILD_SHARED_LIBS=OFF \
    -DGLFW_BUILD_EXAMPLES=OFF \
    -DGLFW_BUILD_TESTS=OFF \
    -DGLFW_BUILD_DOCS=OFF \
    -DCMAKE_INSTALL_PREFIX=/glfw_install

RUN make -j$(nproc)
RUN make install

RUN mkdir -p /archive/lib
RUN cp /glfw_install/lib/libglfw3.a /archive/lib/
RUN cp -r /glfw_install/include /archive/
ADD ./cmake/CMakeLists.txt /archive/CMakeLists.txt

WORKDIR /archive
RUN tar -zcvf /archive.tar.gz **

ENTRYPOINT [ "cp", "/archive.tar.gz", "/out/archive.tar.gz" ]
