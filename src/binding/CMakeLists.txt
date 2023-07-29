# A basic hello world.
add_library(binding MODULE examples_bindings.c examples.c binding_module.c wrappers.h)
target_link_libraries(binding error_codes)
install_python_target(binding src/binding)

add_subdirectory(tests)
add_subdirectory(benchmarks)
