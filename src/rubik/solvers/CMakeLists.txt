add_subdirectory(tests)
add_subdirectory(demos)

add_library(solvers INTERFACE)
target_link_libraries(solvers INTERFACE paths shapes)
