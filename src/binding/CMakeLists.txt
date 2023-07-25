# A basic hello world.
add_library(binding MODULE binding.c)
install_python_target(binding src/binding)

add_subdirectory(test)
