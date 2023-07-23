# Building 

[TOC]

## Building from source

We follow the CMake convention by only encouraging "out-of-source"
builds, hence the reason for this build directory existing.
This directory exists only for manual building and testing with `cmake` et al.

To build the project:
```bash
cd build
cmake .. 
make 
make test
ctest 
```
!!! note
    `make test` and `ctest` are synonymous.

### Modern C23 compilers

We are trying to use a very modern C standard
(C23 is brand new at the time of writing), and compiler
support for this is very limited. To ensure `cmake` can find
a sufficiently new compiler version, it may be necessary to
hard wire paths to these in your invocation of `cmake`, e.g.:

```bash
cmake -D CMAKE_C_COMPILER=/usr/local/Cellar/gcc/13.1.0/bin/gcc-13 -D CMAKE_CXX_COMPILER=/usr/local/Cellar/gcc/13.1.0/bin/g++-13 ..
```

## Debugging

If any tests are failing, then these
can be debugged further by running
```bash
ctest --rerun-failed --output-on-failure
```