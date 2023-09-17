add_subdirectory(tests)

add_library(paths path.cpp)
target_link_libraries(paths logging)
