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
include src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/compiler_depend.make

# Include the progress variables for this target.
include src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/progress.make

# Include the compile flags for this target's objects.
include src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/flags.make

src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.o: src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/flags.make
src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.o: /Users/oliver/ClionProjects/testing/src/rubiks/paths/tests/paths.cpp
src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.o: src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.o -MF CMakeFiles/paths_cpp.dir/paths.cpp.o.d -o CMakeFiles/paths_cpp.dir/paths.cpp.o -c /Users/oliver/ClionProjects/testing/src/rubiks/paths/tests/paths.cpp

src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/paths_cpp.dir/paths.cpp.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/oliver/ClionProjects/testing/src/rubiks/paths/tests/paths.cpp > CMakeFiles/paths_cpp.dir/paths.cpp.i

src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/paths_cpp.dir/paths.cpp.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/oliver/ClionProjects/testing/src/rubiks/paths/tests/paths.cpp -o CMakeFiles/paths_cpp.dir/paths.cpp.s

# Object files for target paths_cpp
paths_cpp_OBJECTS = \
"CMakeFiles/paths_cpp.dir/paths.cpp.o"

# External object files for target paths_cpp
paths_cpp_EXTERNAL_OBJECTS =

src/rubiks/paths/tests/paths_cpp: src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/paths.cpp.o
src/rubiks/paths/tests/paths_cpp: src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/build.make
src/rubiks/paths/tests/paths_cpp: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
src/rubiks/paths/tests/paths_cpp: src/rubiks/paths/libpaths.a
src/rubiks/paths/tests/paths_cpp: /usr/local/lib/libgtest_main.a
src/rubiks/paths/tests/paths_cpp: /usr/local/lib/libgtest.a
src/rubiks/paths/tests/paths_cpp: src/rubiks/paths/libpaths.a
src/rubiks/paths/tests/paths_cpp: src/rubiks/colours/libcolours.a
src/rubiks/paths/tests/paths_cpp: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
src/rubiks/paths/tests/paths_cpp: /usr/local/lib/libglog.0.6.0.dylib
src/rubiks/paths/tests/paths_cpp: /usr/local/lib/libgflags.2.2.2.dylib
src/rubiks/paths/tests/paths_cpp: src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable paths_cpp"
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/paths_cpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/build: src/rubiks/paths/tests/paths_cpp
.PHONY : src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/build

src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests && $(CMAKE_COMMAND) -P CMakeFiles/paths_cpp.dir/cmake_clean.cmake
.PHONY : src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/clean

src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/depend:
	cd /Users/oliver/ClionProjects/testing/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/rubiks/paths/tests /Users/oliver/ClionProjects/testing/cmake-build-debug /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/rubiks/paths/tests/CMakeFiles/paths_cpp.dir/depend

