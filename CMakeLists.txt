cmake_minimum_required(VERSION 3.25)
project(testing C CXX)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 23)

# So we can find modules in the project root. (e.g. Criterion)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/")
find_package(Criterion REQUIRED)

add_executable(hello_world hello_world.c)

enable_testing()
add_executable(test_example test_example.c)
target_link_libraries(test_example PRIVATE criterion)
add_test(NAME test_example COMMAND test_example)

add_executable(main main.cpp my_stacks.hpp my_queues.hpp my_minimum.hpp) # my_sort.hpp my_sort.cpp)

# Trying to add logging.
PKG_CHECK_MODULES(GLIB REQUIRED glib-2.0)

INCLUDE_DIRECTORIES(src/include/ ${GLIB_INCLUDE_DIRS})

#LINK_DIRECTORIES(${GLIB_LIBRARY_DIRS})
add_executable(example_logging example_logging.c)
TARGET_LINK_LIBRARIES(example_logging ${GLIB_LIBRARIES})

add_executable(example_logging_cpp example_logging.cpp)
TARGET_LINK_LIBRARIES(example_logging_cpp ${GLIB_LIBRARIES})
