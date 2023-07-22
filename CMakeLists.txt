cmake_minimum_required(VERSION 3.25)  # Use the latest and greatest.
project(testing C CXX) # We use a mix of C and C++.

# We want to use the latest standards.
set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 23)
set(ERROR_FLAGS  "-Wall -Wextra -Werror -pedantic -Wno-int-conversion -Wno-missing-field-initializers -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function")
set(CMAKE_C_FLAGS  "${CMAKE_C_FLAGS} ${ERROR_FLAGS}")
set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${ERROR_FLAGS}")

include(CheckCCompilerFlag)
CHECK_C_COMPILER_FLAG("-std=c2x" COMPILER_SUPPORTS_C2X)
if(COMPILER_SUPPORTS_C2X)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c2x")
else()
    message(FATAL_ERROR "Compiler ${CMAKE_C_COMPILER} has no C2X support.")
endif()

# To enable testing and use of ctest.
enable_testing()
# ^ This must be before any calls to add_subdirectory to ensure it is enabled recursively.
# cf. https://stackoverflow.com/questions/54550939/ctest-add-tests-in-subdirectories#comment109191766_55835742

# Where we find the source files for our builds.
add_subdirectory(src)

# Some C++ examples.
#add_executable(main main.cpp my_stacks.hpp my_queues.hpp my_minimum.hpp) # my_sort.hpp my_sort.cpp)




