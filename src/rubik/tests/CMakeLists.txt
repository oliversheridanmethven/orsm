add_all_python_tests()


add_executable(shapes_cpp shapes.cpp)
target_link_libraries(shapes_cpp testing shapes)
add_test(NAME shapes_cpp COMMAND shapes_cpp)
