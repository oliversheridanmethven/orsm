add_subdirectory(tests)

find_package(PkgConfig REQUIRED)
pkg_search_module(GLIB REQUIRED glib-2.0)
add_library(logging INTERFACE)
target_include_directories(logging SYSTEM INTERFACE ${GLIB_INCLUDE_DIRS})
target_include_directories(logging INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)
target_link_libraries(logging INTERFACE ${GLIB_LIBRARIES})
target_compile_options(logging INTERFACE -Wno-constant-logical-operand)  # GLib can trigger this error with some compilers.

