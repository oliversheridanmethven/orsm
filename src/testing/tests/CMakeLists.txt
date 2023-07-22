
add_executable(test_example test_example.c)
target_link_libraries(test_example PRIVATE testing)
target_include_directories(test_example PUBLIC "${PROJECT_BINARY_DIR}" "${PROJECT_SOURCE_DIR}/testing")
add_test(NAME test_example COMMAND test_example)


#
#add_executable(test_example test_example.c)
#target_link_libraries(test_example PRIVATE criterion)
#add_test(NAME test_example COMMAND test_example)