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
CMAKE_BINARY_DIR = /Users/oliver/ClionProjects/testing/cmake-build-release-2

# Include any dependencies generated for this target.
include src/rubik/paths/CMakeFiles/paths.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/rubik/paths/CMakeFiles/paths.dir/compiler_depend.make

# Include the progress variables for this target.
include src/rubik/paths/CMakeFiles/paths.dir/progress.make

# Include the compile flags for this target's objects.
include src/rubik/paths/CMakeFiles/paths.dir/flags.make

src/rubik/paths/CMakeFiles/paths.dir/path.cpp.o: src/rubik/paths/CMakeFiles/paths.dir/flags.make
src/rubik/paths/CMakeFiles/paths.dir/path.cpp.o: /Users/oliver/ClionProjects/testing/src/rubik/paths/path.cpp
src/rubik/paths/CMakeFiles/paths.dir/path.cpp.o: src/rubik/paths/CMakeFiles/paths.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release-2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/rubik/paths/CMakeFiles/paths.dir/path.cpp.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/rubik/paths/CMakeFiles/paths.dir/path.cpp.o -MF CMakeFiles/paths.dir/path.cpp.o.d -o CMakeFiles/paths.dir/path.cpp.o -c /Users/oliver/ClionProjects/testing/src/rubik/paths/path.cpp

src/rubik/paths/CMakeFiles/paths.dir/path.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/paths.dir/path.cpp.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/oliver/ClionProjects/testing/src/rubik/paths/path.cpp > CMakeFiles/paths.dir/path.cpp.i

src/rubik/paths/CMakeFiles/paths.dir/path.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/paths.dir/path.cpp.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/oliver/ClionProjects/testing/src/rubik/paths/path.cpp -o CMakeFiles/paths.dir/path.cpp.s

# Object files for target paths
paths_OBJECTS = \
"CMakeFiles/paths.dir/path.cpp.o"

# External object files for target paths
paths_EXTERNAL_OBJECTS =

src/rubik/paths/libpaths.a: src/rubik/paths/CMakeFiles/paths.dir/path.cpp.o
src/rubik/paths/libpaths.a: src/rubik/paths/CMakeFiles/paths.dir/build.make
src/rubik/paths/libpaths.a: src/rubik/paths/CMakeFiles/paths.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release-2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libpaths.a"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths && $(CMAKE_COMMAND) -P CMakeFiles/paths.dir/cmake_clean_target.cmake
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/paths.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/rubik/paths/CMakeFiles/paths.dir/build: src/rubik/paths/libpaths.a
.PHONY : src/rubik/paths/CMakeFiles/paths.dir/build

src/rubik/paths/CMakeFiles/paths.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths && $(CMAKE_COMMAND) -P CMakeFiles/paths.dir/cmake_clean.cmake
.PHONY : src/rubik/paths/CMakeFiles/paths.dir/clean

src/rubik/paths/CMakeFiles/paths.dir/depend:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/rubik/paths /Users/oliver/ClionProjects/testing/cmake-build-release-2 /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/paths/CMakeFiles/paths.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/rubik/paths/CMakeFiles/paths.dir/depend

