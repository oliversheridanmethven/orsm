add_subdirectory(tests)

add_library(solvers meet_in_middle_recursive.cpp)
target_link_libraries(solvers paths shapes)


add_executable(demo_cpp demo.cpp)
target_link_libraries(demo_cpp logging colours paths solvers common)
