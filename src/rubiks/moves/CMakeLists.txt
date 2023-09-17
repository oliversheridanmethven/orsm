add_subdirectory(tests)

add_library(moves INTERFACE)
target_link_libraries(moves logging)
