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
CMAKE_BINARY_DIR = /Users/oliver/ClionProjects/testing/cmake-build-release

# Include any dependencies generated for this target.
include src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/compiler_depend.make

# Include the progress variables for this target.
include src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/progress.make

# Include the compile flags for this target's objects.
include src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/flags.make

src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.o: src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/flags.make
src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.o: /Users/oliver/ClionProjects/testing/src/rubik/shapes/tests/shapes.cpp
src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.o: src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.o -MF CMakeFiles/shapes_cpp.dir/shapes.cpp.o.d -o CMakeFiles/shapes_cpp.dir/shapes.cpp.o -c /Users/oliver/ClionProjects/testing/src/rubik/shapes/tests/shapes.cpp

src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/shapes_cpp.dir/shapes.cpp.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/oliver/ClionProjects/testing/src/rubik/shapes/tests/shapes.cpp > CMakeFiles/shapes_cpp.dir/shapes.cpp.i

src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/shapes_cpp.dir/shapes.cpp.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/oliver/ClionProjects/testing/src/rubik/shapes/tests/shapes.cpp -o CMakeFiles/shapes_cpp.dir/shapes.cpp.s

# Object files for target shapes_cpp
shapes_cpp_OBJECTS = \
"CMakeFiles/shapes_cpp.dir/shapes.cpp.o"

# External object files for target shapes_cpp
shapes_cpp_EXTERNAL_OBJECTS =

src/rubik/shapes/tests/shapes_cpp: src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/shapes.cpp.o
src/rubik/shapes/tests/shapes_cpp: src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/build.make
src/rubik/shapes/tests/shapes_cpp: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
src/rubik/shapes/tests/shapes_cpp: /usr/local/lib/libgtest_main.a
src/rubik/shapes/tests/shapes_cpp: /usr/local/lib/libgtest.a
src/rubik/shapes/tests/shapes_cpp: src/rubik/paths/libpaths.a
src/rubik/shapes/tests/shapes_cpp: src/rubik/colours/libcolours.a
src/rubik/shapes/tests/shapes_cpp: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
src/rubik/shapes/tests/shapes_cpp: /usr/local/lib/libglog.0.6.0.dylib
src/rubik/shapes/tests/shapes_cpp: /usr/local/lib/libgflags.2.2.2.dylib
src/rubik/shapes/tests/shapes_cpp: src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable shapes_cpp"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/shapes_cpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/build: src/rubik/shapes/tests/shapes_cpp
.PHONY : src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/build

src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests && $(CMAKE_COMMAND) -P CMakeFiles/shapes_cpp.dir/cmake_clean.cmake
.PHONY : src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/clean

src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/depend:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/rubik/shapes/tests /Users/oliver/ClionProjects/testing/cmake-build-release /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/rubik/shapes/tests/CMakeFiles/shapes_cpp.dir/depend

