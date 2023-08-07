add_subdirectory(tests)

# A basic hello world.
add_library(hello_world hello_world.c)
target_include_directories(hello_world INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_executable(hello_world_example hello_world_example.c)
target_link_libraries(hello_world_example hello_world)
