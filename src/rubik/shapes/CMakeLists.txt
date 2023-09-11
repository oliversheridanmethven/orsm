add_subdirectory(tests)
add_subdirectory(utils)

add_library(shapes INTERFACE)
add_dependencies(shapes logging paths colours)
