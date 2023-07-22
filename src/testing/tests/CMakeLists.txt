add_executable(test_example test_example.c)
target_link_libraries(test_example testing)
add_test(NAME test_example COMMAND test_example)