# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/oliver/ClionProjects/testing

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/oliver/ClionProjects/testing

# Include any dependencies generated for this target.
include src/version/CMakeFiles/version_bindings.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/version/CMakeFiles/version_bindings.dir/compiler_depend.make

# Include the progress variables for this target.
include src/version/CMakeFiles/version_bindings.dir/progress.make

# Include the compile flags for this target's objects.
include src/version/CMakeFiles/version_bindings.dir/flags.make

src/version/CMakeFiles/version_bindings.dir/version_bindings.c.o: src/version/CMakeFiles/version_bindings.dir/flags.make
src/version/CMakeFiles/version_bindings.dir/version_bindings.c.o: src/version/version_bindings.c
src/version/CMakeFiles/version_bindings.dir/version_bindings.c.o: src/version/CMakeFiles/version_bindings.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/version/CMakeFiles/version_bindings.dir/version_bindings.c.o"
	cd /Users/oliver/ClionProjects/testing/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/version/CMakeFiles/version_bindings.dir/version_bindings.c.o -MF CMakeFiles/version_bindings.dir/version_bindings.c.o.d -o CMakeFiles/version_bindings.dir/version_bindings.c.o -c /Users/oliver/ClionProjects/testing/src/version/version_bindings.c

src/version/CMakeFiles/version_bindings.dir/version_bindings.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/version_bindings.dir/version_bindings.c.i"
	cd /Users/oliver/ClionProjects/testing/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/oliver/ClionProjects/testing/src/version/version_bindings.c > CMakeFiles/version_bindings.dir/version_bindings.c.i

src/version/CMakeFiles/version_bindings.dir/version_bindings.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/version_bindings.dir/version_bindings.c.s"
	cd /Users/oliver/ClionProjects/testing/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/oliver/ClionProjects/testing/src/version/version_bindings.c -o CMakeFiles/version_bindings.dir/version_bindings.c.s

src/version/CMakeFiles/version_bindings.dir/version_module.c.o: src/version/CMakeFiles/version_bindings.dir/flags.make
src/version/CMakeFiles/version_bindings.dir/version_module.c.o: src/version/version_module.c
src/version/CMakeFiles/version_bindings.dir/version_module.c.o: src/version/CMakeFiles/version_bindings.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object src/version/CMakeFiles/version_bindings.dir/version_module.c.o"
	cd /Users/oliver/ClionProjects/testing/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/version/CMakeFiles/version_bindings.dir/version_module.c.o -MF CMakeFiles/version_bindings.dir/version_module.c.o.d -o CMakeFiles/version_bindings.dir/version_module.c.o -c /Users/oliver/ClionProjects/testing/src/version/version_module.c

src/version/CMakeFiles/version_bindings.dir/version_module.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/version_bindings.dir/version_module.c.i"
	cd /Users/oliver/ClionProjects/testing/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/oliver/ClionProjects/testing/src/version/version_module.c > CMakeFiles/version_bindings.dir/version_module.c.i

src/version/CMakeFiles/version_bindings.dir/version_module.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/version_bindings.dir/version_module.c.s"
	cd /Users/oliver/ClionProjects/testing/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/oliver/ClionProjects/testing/src/version/version_module.c -o CMakeFiles/version_bindings.dir/version_module.c.s

# Object files for target version_bindings
version_bindings_OBJECTS = \
"CMakeFiles/version_bindings.dir/version_bindings.c.o" \
"CMakeFiles/version_bindings.dir/version_module.c.o"

# External object files for target version_bindings
version_bindings_EXTERNAL_OBJECTS =

lib/version_bindings.so: src/version/CMakeFiles/version_bindings.dir/version_bindings.c.o
lib/version_bindings.so: src/version/CMakeFiles/version_bindings.dir/version_module.c.o
lib/version_bindings.so: src/version/CMakeFiles/version_bindings.dir/build.make
lib/version_bindings.so: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
lib/version_bindings.so: lib/libversion.a
lib/version_bindings.so: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
lib/version_bindings.so: src/version/CMakeFiles/version_bindings.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C shared module ../../lib/version_bindings.so"
	cd /Users/oliver/ClionProjects/testing/src/version && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/version_bindings.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/version/CMakeFiles/version_bindings.dir/build: lib/version_bindings.so
.PHONY : src/version/CMakeFiles/version_bindings.dir/build

src/version/CMakeFiles/version_bindings.dir/clean:
	cd /Users/oliver/ClionProjects/testing/src/version && $(CMAKE_COMMAND) -P CMakeFiles/version_bindings.dir/cmake_clean.cmake
.PHONY : src/version/CMakeFiles/version_bindings.dir/clean

src/version/CMakeFiles/version_bindings.dir/depend:
	cd /Users/oliver/ClionProjects/testing && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/version /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/version /Users/oliver/ClionProjects/testing/src/version/CMakeFiles/version_bindings.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/version/CMakeFiles/version_bindings.dir/depend

