add_subdirectory(tests)
add_subdirectory(demos)

add_library(solvers meet_in_middle_recursive.cpp)
target_link_libraries(solvers paths shapes)
