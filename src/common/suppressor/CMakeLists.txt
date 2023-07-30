add_subdirectory(tests)

add_library(suppressor suppressor.c)
target_link_libraries(suppressor error_codes)
target_include_directories(suppressor INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_library(suppressor_bindings MODULE suppressor_bindings.c)
target_link_libraries(suppressor_bindings suppressor)
install_python_target(suppressor_bindings src/common/suppressor)