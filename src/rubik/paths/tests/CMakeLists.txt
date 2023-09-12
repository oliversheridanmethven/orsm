add_executable(paths_cpp paths.cpp)
target_link_libraries(paths_cpp testing paths shapes)
add_test(NAME paths_cpp COMMAND paths_cpp)