cmake_minimum_required(VERSION 3.25)  # Use the latest and greatest.
project(testing C CXX) # We use a mix of C and C++.

# We want to use the latest standards.
set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 23)

# So we can find modules in the project root. (e.g. Criterion)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/")
find_package(Criterion REQUIRED)

# So we can add versioning to our repo
find_package(Git)
add_custom_target(repo_version
        ${CMAKE_COMMAND} -D SRC=${CMAKE_SOURCE_DIR}/version.h.in
        -D DST=${CMAKE_BINARY_DIR}/version.h
        -D GIT_EXECUTABLE=${GIT_EXECUTABLE}
        -P ${CMAKE_SOURCE_DIR}/GenerateVersionHeader.cmake
        )
add_executable(version version.c)
add_dependencies(version repo_version)

# A basic hello world.
add_executable(hello_world hello_world.c)

# To enable testing and use of ctest.
enable_testing()
add_executable(test_example test_example.c)
target_link_libraries(test_example PRIVATE criterion)
add_test(NAME test_example COMMAND test_example)

# Some C++ examples.
add_executable(main main.cpp my_stacks.hpp my_queues.hpp my_minimum.hpp) # my_sort.hpp my_sort.cpp)

# To add logging using GLIB.
PKG_CHECK_MODULES(GLIB REQUIRED glib-2.0)
INCLUDE_DIRECTORIES(src/include/ ${GLIB_INCLUDE_DIRS})
add_executable(example_logging example_logging.c)
TARGET_LINK_LIBRARIES(example_logging ${GLIB_LIBRARIES})
add_executable(example_logging_cpp example_logging.cpp)
TARGET_LINK_LIBRARIES(example_logging_cpp ${GLIB_LIBRARIES})

# To add the command line argument parser.
add_executable(cli_arguments cli_arguments.c)
target_link_libraries(cli_arguments PRIVATE argp)


