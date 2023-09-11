add_subdirectory(tests)
add_subdirectory(demos)

add_library(solvers INTERFACE)
add_dependencies(solvers paths shapes)
