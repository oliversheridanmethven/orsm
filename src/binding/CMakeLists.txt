# A basic hello world.
add_library(examples examples.c)
target_link_libraries(examples error_codes)
add_library(binding MODULE examples_bindings.c binding_module.c wrappers.h)
target_link_libraries(binding examples)
install_python_target(binding src/binding)

add_subdirectory(tests)
add_subdirectory(benchmarks)
