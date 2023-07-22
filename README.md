# Testing

## Author

Dr Oliver Sheridan-Methven 
[oliver.sheridan-methven@hotmail.co.uk](mailto:oliver.sheridan-methven@hotmail.co.uk).

## Description

A collection of various code snippets designed for me to 
test various ideas and code snippets, akin to a code scratch
space. 

## Setting up the repo

### Dependencies

The project relies on a few dependencies, the most notable of 
which include:

- GCC (with C23 and C++23 support).
- CMake.
- GLIB (for logging).
- Argp (for the CLI).
- Criterion (for testing).

### Build

To build the project:
```bash
cd build
cmake .. 
make 
make test
ctest 
```
> NB: `make test` and `ctest` are synonymous. 

>We are trying to use a very modern C standard
> (C23 is brand new at the time of writing), and compiler
> support for this is very limited. To ensure `cmake` can find
> a sufficiently new compiler version, it may be necessary to
> hard wire paths to these in your invocation of `cmake`, e.g.:  
> ```
> cmake -D CMAKE_C_COMPILER=/usr/local/Cellar/gcc/13.1.0/bin/gcc-13 -D CMAKE_CXX_COMPILER=/usr/local/Cellar/gcc/13.1.0/bin/g++-13 ..
> ```

If any tests are failing, then these 
can be debugged further by running
```bash
ctest --rerun-failed --output-on-failure
```




