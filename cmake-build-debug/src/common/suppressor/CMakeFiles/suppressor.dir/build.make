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
CMAKE_BINARY_DIR = /Users/oliver/ClionProjects/testing/cmake-build-debug

# Include any dependencies generated for this target.
include src/common/suppressor/CMakeFiles/suppressor.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/common/suppressor/CMakeFiles/suppressor.dir/compiler_depend.make

# Include the progress variables for this target.
include src/common/suppressor/CMakeFiles/suppressor.dir/progress.make

# Include the compile flags for this target's objects.
include src/common/suppressor/CMakeFiles/suppressor.dir/flags.make

src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.o: src/common/suppressor/CMakeFiles/suppressor.dir/flags.make
src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.o: /Users/oliver/ClionProjects/testing/src/common/suppressor/suppressor.c
src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.o: src/common/suppressor/CMakeFiles/suppressor.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.o -MF CMakeFiles/suppressor.dir/suppressor.c.o.d -o CMakeFiles/suppressor.dir/suppressor.c.o -c /Users/oliver/ClionProjects/testing/src/common/suppressor/suppressor.c

src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/suppressor.dir/suppressor.c.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/oliver/ClionProjects/testing/src/common/suppressor/suppressor.c > CMakeFiles/suppressor.dir/suppressor.c.i

src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/suppressor.dir/suppressor.c.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/oliver/ClionProjects/testing/src/common/suppressor/suppressor.c -o CMakeFiles/suppressor.dir/suppressor.c.s

# Object files for target suppressor
suppressor_OBJECTS = \
"CMakeFiles/suppressor.dir/suppressor.c.o"

# External object files for target suppressor
suppressor_EXTERNAL_OBJECTS =

src/common/suppressor/libsuppressor.a: src/common/suppressor/CMakeFiles/suppressor.dir/suppressor.c.o
src/common/suppressor/libsuppressor.a: src/common/suppressor/CMakeFiles/suppressor.dir/build.make
src/common/suppressor/libsuppressor.a: src/common/suppressor/CMakeFiles/suppressor.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libsuppressor.a"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor && $(CMAKE_COMMAND) -P CMakeFiles/suppressor.dir/cmake_clean_target.cmake
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/suppressor.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/common/suppressor/CMakeFiles/suppressor.dir/build: src/common/suppressor/libsuppressor.a
.PHONY : src/common/suppressor/CMakeFiles/suppressor.dir/build

src/common/suppressor/CMakeFiles/suppressor.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor && $(CMAKE_COMMAND) -P CMakeFiles/suppressor.dir/cmake_clean.cmake
.PHONY : src/common/suppressor/CMakeFiles/suppressor.dir/clean

src/common/suppressor/CMakeFiles/suppressor.dir/depend:
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/common/suppressor /Users/oliver/ClionProjects/testing/cmake-build-debug /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor /Users/oliver/ClionProjects/testing/cmake-build-debug/src/common/suppressor/CMakeFiles/suppressor.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/common/suppressor/CMakeFiles/suppressor.dir/depend

