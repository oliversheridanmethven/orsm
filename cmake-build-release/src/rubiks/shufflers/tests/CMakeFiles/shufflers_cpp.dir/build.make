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
include src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/compiler_depend.make

# Include the progress variables for this target.
include src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/progress.make

# Include the compile flags for this target's objects.
include src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/flags.make

src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o: src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/flags.make
src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o: /Users/oliver/ClionProjects/testing/src/rubiks/shufflers/tests/shufflers.cpp
src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o: src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o -MF CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o.d -o CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o -c /Users/oliver/ClionProjects/testing/src/rubiks/shufflers/tests/shufflers.cpp

src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/shufflers_cpp.dir/shufflers.cpp.i"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/oliver/ClionProjects/testing/src/rubiks/shufflers/tests/shufflers.cpp > CMakeFiles/shufflers_cpp.dir/shufflers.cpp.i

src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/shufflers_cpp.dir/shufflers.cpp.s"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests && /usr/local/opt/llvm/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/oliver/ClionProjects/testing/src/rubiks/shufflers/tests/shufflers.cpp -o CMakeFiles/shufflers_cpp.dir/shufflers.cpp.s

# Object files for target shufflers_cpp
shufflers_cpp_OBJECTS = \
"CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o"

# External object files for target shufflers_cpp
shufflers_cpp_EXTERNAL_OBJECTS =

src/rubiks/shufflers/tests/shufflers_cpp: src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/shufflers.cpp.o
src/rubiks/shufflers/tests/shufflers_cpp: src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/build.make
src/rubiks/shufflers/tests/shufflers_cpp: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
src/rubiks/shufflers/tests/shufflers_cpp: src/rubiks/colours/libcolours.a
src/rubiks/shufflers/tests/shufflers_cpp: src/rubiks/paths/libpaths.a
src/rubiks/shufflers/tests/shufflers_cpp: /usr/local/lib/libgtest_main.a
src/rubiks/shufflers/tests/shufflers_cpp: /usr/local/lib/libgtest.a
src/rubiks/shufflers/tests/shufflers_cpp: /Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
src/rubiks/shufflers/tests/shufflers_cpp: /usr/local/lib/libglog.0.6.0.dylib
src/rubiks/shufflers/tests/shufflers_cpp: /usr/local/lib/libgflags.2.2.2.dylib
src/rubiks/shufflers/tests/shufflers_cpp: src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/oliver/ClionProjects/testing/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable shufflers_cpp"
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/shufflers_cpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/build: src/rubiks/shufflers/tests/shufflers_cpp
.PHONY : src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/build

src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/clean:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests && $(CMAKE_COMMAND) -P CMakeFiles/shufflers_cpp.dir/cmake_clean.cmake
.PHONY : src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/clean

src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/depend:
	cd /Users/oliver/ClionProjects/testing/cmake-build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/oliver/ClionProjects/testing /Users/oliver/ClionProjects/testing/src/rubiks/shufflers/tests /Users/oliver/ClionProjects/testing/cmake-build-release /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests /Users/oliver/ClionProjects/testing/cmake-build-release/src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/rubiks/shufflers/tests/CMakeFiles/shufflers_cpp.dir/depend

