add_executable(example example.c)
target_link_libraries(example testing)
add_test(NAME example COMMAND example)

find_package(Python COMPONENTS Interpreter REQUIRED)
add_test(NAME basic_python_test COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_basic_python.py)