add_subdirectory(tests)

add_library(shufflers INTERFACE)
target_link_libraries(shufflers INTERFACE paths shapes)