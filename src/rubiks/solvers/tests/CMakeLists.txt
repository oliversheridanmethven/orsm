add_all_python_tests()

add_executable(solvers_cpp solvers.cpp)
target_link_libraries(solvers_cpp testing solvers shapes colours paths)
add_test(NAME solvers_cpp COMMAND solvers_cpp)
