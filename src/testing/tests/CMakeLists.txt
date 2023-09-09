add_executable(example example.c)
target_link_libraries(example testing)
add_test(NAME example COMMAND example)

add_python_tests(basic_python.py basic_python_again.py)

add_executable(example_cpp example.cpp)
target_link_libraries(example_cpp testing)
add_test(NAME example_cpp COMMAND example_cpp)
