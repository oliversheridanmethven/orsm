add_executable(_suppressor suppressor.c)
target_link_libraries(_suppressor testing suppressor)
add_test(NAME suppressor COMMAND _suppressor)