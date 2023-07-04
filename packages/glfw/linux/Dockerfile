FROM debian:10

ARG PACKAGE
ARG VERSION
ARG CC_COMPILER_PACKAGE
ARG CXX_COMPILER_PACKAGE
ARG CC_COMPILER
ARG CXX_COMPILER
ARG TOOLCHAIN_FILE

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libx11-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev
RUN apt-get install -y make cmake git
RUN apt-get install -y $CC_COMPILER_PACKAGE $CXX_COMPILER_PACKAGE

ENV PACKAGE=$PACKAGE
ENV VERSION=$VERSION
ENV CC=$CC_COMPILER
ENV CXX=$CXX_COMPILER
ENV TOOLCHAIN_FILE=$TOOLCHAIN_FILE
ENTRYPOINT [ "/package/build.sh" ]