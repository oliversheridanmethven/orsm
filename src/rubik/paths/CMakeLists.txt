add_subdirectory(tests)

add_library(paths paths.cpp)
target_link_libraries(paths logging)
