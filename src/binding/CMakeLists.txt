# A basic hello world.
add_library(binding MODULE hello_world.c)
install_python_target(binding src/binding)

add_subdirectory(test)
