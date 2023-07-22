add_subdirectory(tests)

## So we can find modules in the project root. (e.g. Criterion)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/")
find_package(Criterion REQUIRED)

add_library(testing testing.c)

#add_executable(test_example test_example.c)
#target_link_libraries(test_example PRIVATE criterion)
#add_test(NAME test_example COMMAND test_example)