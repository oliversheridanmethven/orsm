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
include src/rubik/colours/CMakeFiles/colours.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/rubik/colours/CMakeFiles/colours.dir/compiler_depend.make

# Include the progress variables for this target.
include src/rubik/colours/CMakeFiles/colours.dir/progress.make

# Include the compile flags for this target's objects.
include src/rubik/colours/CMakeFiles/colours.dir/flags.make

src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.o: src/rubik/colours/CMakeFiles/colours.dir/flags.make
src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.o: /Users/oliver/ClionProjects/testing/src/rubik/colours/colour_palette.cpp
src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.o: src/rubik/colours/CMakeFiles/colours.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release-2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.o -MF CMakeFiles/colours.dir/colour_palette.cpp.o.d -o CMakeFiles/colours.dir/colour_palette.cpp.o -c /Users/oliver/ClionProjects/testing/src/rubik/colours/colour_palette.cpp

src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/colours.dir/colour_palette.cpp.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/oliver/ClionProjects/testing/src/rubik/colours/colour_palette.cpp > CMakeFiles/colours.dir/colour_palette.cpp.i

src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/colours.dir/colour_palette.cpp.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/oliver/ClionProjects/testing/src/rubik/colours/colour_palette.cpp -o CMakeFiles/colours.dir/colour_palette.cpp.s

# Object files for target colours
colours_OBJECTS = \
"CMakeFiles/colours.dir/colour_palette.cpp.o"

# External object files for target colours
colours_EXTERNAL_OBJECTS =

src/rubik/colours/libcolours.a: src/rubik/colours/CMakeFiles/colours.dir/colour_palette.cpp.o
src/rubik/colours/libcolours.a: src/rubik/colours/CMakeFiles/colours.dir/build.make
src/rubik/colours/libcolours.a: src/rubik/colours/CMakeFiles/colours.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release-2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libcolours.a"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours && $(CMAKE_COMMAND) -P CMakeFiles/colours.dir/cmake_clean_target.cmake
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/colours.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/rubik/colours/CMakeFiles/colours.dir/build: src/rubik/colours/libcolours.a
.PHONY : src/rubik/colours/CMakeFiles/colours.dir/build

src/rubik/colours/CMakeFiles/colours.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours && $(CMAKE_COMMAND) -P CMakeFiles/colours.dir/cmake_clean.cmake
.PHONY : src/rubik/colours/CMakeFiles/colours.dir/clean

src/rubik/colours/CMakeFiles/colours.dir/depend:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release-2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/rubik/colours /Users/oliver/ClionProjects/testing/cmake-build-release-2 /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours /Users/oliver/ClionProjects/testing/cmake-build-release-2/src/rubik/colours/CMakeFiles/colours.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/rubik/colours/CMakeFiles/colours.dir/depend

