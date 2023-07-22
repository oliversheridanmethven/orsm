add_subdirectory(tests)

# So we can add versioning to our repo
find_package(Git)
add_custom_target(repo_version
        ${CMAKE_COMMAND} -D SRC=${CMAKE_CURRENT_SOURCE_DIR}/version.h.in
        -D DST=${CMAKE_CURRENT_BINARY_DIR}/version.h
        -D GIT_EXECUTABLE=${GIT_EXECUTABLE}
        -D CMAKE_PROJECT_NAME=${CMAKE_PROJECT_NAME}
        -P ${CMAKE_CURRENT_SOURCE_DIR}/GenerateVersionHeader.cmake
        )

add_library(version INTERFACE)
add_dependencies(version repo_version)
#target_include_directories(lib1 INTERFACE
#        "${PROJECT_SOURCE_DIR}/lib1"
#        )



