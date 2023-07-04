FROM ghcr.io/rektinator/msbuild-docker:latest
USER 0

RUN vs_cmd "cmd /c exit 0"   # Run vs_cmd once to initialize wine

RUN apt-get update && apt-get install -y git curl
# RUN apt-get update && apt-get install -y git curl p7zip-full python3 && rm -r /var/lib/apt/lists/*
# RUN mkdir /choco
# RUN curl https://github.com/PietJankbal/Chocolatey-for-wine/releases/download/v0.5c.715/Chocolatey-for-wine.7z -o /choco/Chocolatey-for-wine.7z
# RUN ls /choco
# RUN 7z x /choco/Chocolatey-for-wine.7z -o/choco/unpacked
# RUN wine /choco/ChoCinstaller_0.5y.703.exe


ARG PACKAGE
ARG VERSION
ARG CC_COMPILER_PACKAGE
ARG CXX_COMPILER_PACKAGE
ARG CC_COMPILER
ARG CXX_COMPILER
ARG TOOLCHAIN_FILE
ARG GIT_REPOSITORY

ENV PACKAGE=$PACKAGE
ENV VERSION=$VERSION
ENV CC=$CC_COMPILER
ENV CXX=$CXX_COMPILER
ENV TOOLCHAIN_FILE=$TOOLCHAIN_FILE
ENV GIT_REPOSITORY=$GIT_REPOSITORY

ENTRYPOINT [ "/repo/scripts/build-win.sh" ]