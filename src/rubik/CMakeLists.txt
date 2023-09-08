add_subdirectory(colours)
add_subdirectory(paths)
add_subdirectory(shapes)
add_subdirectory(shuffles)
add_subdirectory(solvers)

add_library(rubik INTERFACE)
target_include_directories(rubik INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)
