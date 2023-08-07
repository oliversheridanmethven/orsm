# In source builds


## Why allow in source builds?

In source builds are largely discouraged, and are only 
recommended for use by developers. The reason we support this 
for developers is to populate the source directory with various 
generated files, libraries, etc. The use of this is for example:
placing python extension libraries in the source directory. 
This allowed for them to be picked up by an interpreter
which can point to the in source code, rather than what is 
produced by the scikit build procedure. This means code
which is under development can be more easily accessed by
an IDE or interpreter. 

## Making in source builds

From the projects root directory run 
```bash
cmake .
make 
make install
make test 
```

!!! note 
    This is run from the project's root directory, not from a 
    separate dedicated build directory.

# Cleaning everything up

To clean everything up, run 
```bash
make clean
./cmake_uninstall.sh
```
