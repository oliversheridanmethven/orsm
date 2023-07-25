add_executable(example example.c)
target_link_libraries(example testing)
add_test(NAME example COMMAND example)

add_python_test(test_basic_python.py)
add_python_test(test_basic_python_again.py)
