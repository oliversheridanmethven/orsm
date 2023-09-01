add_subdirectory(tests)

# A basic hello world.
add_library(hello_world_c hello_world.c)
target_include_directories(hello_world_c INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_library(hello_world_cpp hello_world.cpp)
target_include_directories(hello_world_cpp INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_executable(hello_world_example_c hello_world_example.c)
target_link_libraries(hello_world_example_c hello_world_c)

add_executable(hello_world_example_cpp hello_world_example.cpp)
target_link_libraries(hello_world_example_cpp hello_world_cpp)
