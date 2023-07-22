cmake_minimum_required(VERSION 3.25)  # Use the latest and greatest.
project(testing C CXX) # We use a mix of C and C++.

# We want to use the latest standards.
set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 23)

# To enable testing and use of ctest.
enable_testing()
# ^ This must be before any calls to add_subdirectory to ensure it is enabled recursively.
# cf. https://stackoverflow.com/questions/54550939/ctest-add-tests-in-subdirectories#comment109191766_55835742



# Where we find the source files for our builds.
add_subdirectory(src)
## A basic hello world.
#add_executable(hello_world hello_world.c)

# Some C++ examples.
add_executable(main main.cpp my_stacks.hpp my_queues.hpp my_minimum.hpp) # my_sort.hpp my_sort.cpp)




