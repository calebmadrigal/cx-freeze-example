# cx-freeze-example

Example of using cx_Freeze to turn a python script into a distributable native binary.

## Usage

#### Build

    python setup.py build

The distributable binary will be in the build folder. Note that this single config will build for Windows, OS X, and Linux.

#### Distribute

In order to distribute, you must copy not only the binary, but the directory that contains it, which contains necessary support files.

