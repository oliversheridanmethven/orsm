add_executable(version_example version.c)
#target_include_directories(version_example PUBLIC "${PROJECT_BINARY_DIR}" "${PROJECT_SOURCE_DIR}")
target_link_libraries(version_example version)
#add_dependencies(version_example version)