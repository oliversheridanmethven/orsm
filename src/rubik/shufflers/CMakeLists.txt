add_subdirectory(tests)
add_subdirectory(demos)

add_library(shufflers INTERFACE)
add_dependencies(shufflers paths shapes)