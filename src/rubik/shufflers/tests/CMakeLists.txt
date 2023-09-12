add_all_python_tests()

add_executable(shufflers_cpp shufflers.cpp)
target_link_libraries(shufflers_cpp testing shapes colours paths)
add_test(NAME shufflers_cpp COMMAND shufflers_cpp)