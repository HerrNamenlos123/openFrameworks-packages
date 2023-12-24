# openFrameworks-packages
Repository just for testing CI stuff

Every package and its building container has the following structure:
 - The entire packages repository is mapped into the container as '/repo'
 - The package subfolder is mapped into the container as '/package'
 - Preferrably everything is built within a /tmp folder
 - /tmp/source contains the source code / git repo
 - /tmp/build-debug and /tmp/build-release contain the build files
 - /tmp/install-debug and /tmp/install-release contain the installed files, that are then packaged
 - Specific files are copied into /tmp/archive-debug and /tmp/archive-release
 - These folders are then compressed into .zip or .tar.gz files depending on the platform
 - The archive is then written to an 'out' folder in the package subfolder: '/package/out'
 - This is the end of the docker-compose workflow, the rest is handled by the CI directly

## Building manually

You must have all requirements installed to compile the package.
Run the following command in the root directory of this repository:

```bash
python -m packages.<package>.build # Or 'python3'

#Example:
# python -m packages.libcurl.build
```