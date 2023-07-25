add_subdirectory(test)

find_package(PkgConfig REQUIRED)
pkg_search_module(GLIB REQUIRED glib-2.0)
add_library(logging INTERFACE)
target_include_directories(logging INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/.. ${GLIB_INCLUDE_DIRS})
target_link_libraries(logging INTERFACE ${GLIB_LIBRARIES})
