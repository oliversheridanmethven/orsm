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
include src/version/CMakeFiles/version.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/version/CMakeFiles/version.dir/compiler_depend.make

# Include the progress variables for this target.
include src/version/CMakeFiles/version.dir/progress.make

# Include the compile flags for this target's objects.
include src/version/CMakeFiles/version.dir/flags.make

/Users/oliver/ClionProjects/testing/src/version/version.c:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating /Users/oliver/ClionProjects/testing/src/version/version.c"
	cd /Users/oliver/ClionProjects/testing/src/version && /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -D SRC=/Users/oliver/ClionProjects/testing/src/version/version.c.in -D DST=/Users/oliver/ClionProjects/testing/src/version/version.c -D GIT_EXECUTABLE=/usr/local/bin/git -D CMAKE_PROJECT_NAME=testing -P /Users/oliver/ClionProjects/testing/src/version/GenerateVersionHeader.cmake

src/version/CMakeFiles/version.dir/version.c.o: src/version/CMakeFiles/version.dir/flags.make
src/version/CMakeFiles/version.dir/version.c.o: /Users/oliver/ClionProjects/testing/src/version/version.c
src/version/CMakeFiles/version.dir/version.c.o: src/version/CMakeFiles/version.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object src/version/CMakeFiles/version.dir/version.c.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/version/CMakeFiles/version.dir/version.c.o -MF CMakeFiles/version.dir/version.c.o.d -o CMakeFiles/version.dir/version.c.o -c /Users/oliver/ClionProjects/testing/src/version/version.c

src/version/CMakeFiles/version.dir/version.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/version.dir/version.c.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/oliver/ClionProjects/testing/src/version/version.c > CMakeFiles/version.dir/version.c.i

src/version/CMakeFiles/version.dir/version.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/version.dir/version.c.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version && /usr/local/bin/gcc-13 $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/oliver/ClionProjects/testing/src/version/version.c -o CMakeFiles/version.dir/version.c.s

# Object files for target version
version_OBJECTS = \
"CMakeFiles/version.dir/version.c.o"

# External object files for target version
version_EXTERNAL_OBJECTS =

src/version/libversion.a: src/version/CMakeFiles/version.dir/version.c.o
src/version/libversion.a: src/version/CMakeFiles/version.dir/build.make
src/version/libversion.a: src/version/CMakeFiles/version.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C static library libversion.a"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version && $(CMAKE_COMMAND) -P CMakeFiles/version.dir/cmake_clean_target.cmake
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/version.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/version/CMakeFiles/version.dir/build: src/version/libversion.a
.PHONY : src/version/CMakeFiles/version.dir/build

src/version/CMakeFiles/version.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version && $(CMAKE_COMMAND) -P CMakeFiles/version.dir/cmake_clean.cmake
.PHONY : src/version/CMakeFiles/version.dir/clean

src/version/CMakeFiles/version.dir/depend: /Users/oliver/ClionProjects/testing/src/version/version.c
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/version /Users/oliver/ClionProjects/testing/cmake-build-debug /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version /Users/oliver/ClionProjects/testing/cmake-build-debug/src/version/CMakeFiles/version.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/version/CMakeFiles/version.dir/depend

