add_library(suppressor MODULE suppressor_bindings.c suppressor.c)
target_link_libraries(suppressor error_codes)
install_python_target(suppressor src/common/suppressor)