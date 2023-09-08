add_subdirectory(tests)

add_library(shapes INTERFACE)
target_link_libraries(shapes INTERFACE logging paths colours)
