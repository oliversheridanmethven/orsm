add_subdirectory(tests)

# So we can add versioning to our repo
find_package(Git)
add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/version.h
        COMMAND ${CMAKE_COMMAND} -D SRC=${CMAKE_CURRENT_SOURCE_DIR}/version.h.in
                -D DST=${CMAKE_CURRENT_BINARY_DIR}/version.h
                -D GIT_EXECUTABLE=${GIT_EXECUTABLE}
                -D CMAKE_PROJECT_NAME=${CMAKE_PROJECT_NAME}
                -P ${CMAKE_CURRENT_SOURCE_DIR}/GenerateVersionHeader.cmake
)

add_library(version INTERFACE)
target_include_directories(version INTERFACE ${CMAKE_CURRENT_BINARY_DIR}/..)
# ^ We use the parent directory so it has to be included in the #include statement




