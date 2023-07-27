# A basic hello world.
add_library(binding MODULE examples_bindings.c examples.c binding_module.c)
install_python_target(binding src/binding)

add_subdirectory(test)
