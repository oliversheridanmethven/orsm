cmake_minimum_required(VERSION 3.25)  # Use the latest and greatest.
project(testing C CXX) # We use a mix of C and C++.

# We want to use the latest standards.
set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)
# Only some of the latest and greatest compilers offer the appropriate level of support.
set(CMAKE_C_COMPILER "gcc-13")
set(CC ${CMAKE_C_COMPILER})
#set(CMAKE_C_COMPILER "clang-16")
set(CMAKE_CXX_STANDARD 23)
set(ERROR_FLAGS "-Wall -Wextra -Werror -pedantic -Wno-int-conversion -Wno-missing-field-initializers -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function")
message(DEBUG "The C compiler flags are: ${CMAKE_C_FLAGS}")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${ERROR_FLAGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${ERROR_FLAGS}")

if("${PROJECT_SOURCE_DIR}" STREQUAL "${PROJECT_BINARY_DIR}")
    message(STATUS "Producing an in-source build. (This is only recommended for developers!).")
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
endif()


include(CheckCCompilerFlag)
CHECK_C_COMPILER_FLAG("-std=c2x" COMPILER_SUPPORTS_C2X)
if(COMPILER_SUPPORTS_C2X)
    message(STATUS "Compiler ${CMAKE_C_COMPILER} appears to have C2X support.")
    foreach(i ${CMAKE_C_COMPILE_FEATURES})
        message(DEBUG "Compiler ${CMAKE_C_COMPILER} uses feature: ${i}")
    endforeach()
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c2x")
else()
    message(FATAL_ERROR "Compiler ${CMAKE_C_COMPILER} has no C2X support.")
endif()

# To enable testing and use of ctest.
enable_testing()
# ^ This must be before any calls to add_subdirectory to ensure it is enabled recursively.
# cf. https://stackoverflow.com/questions/54550939/ctest-add-tests-in-subdirectories#comment109191766_55835742

# We use scikit-build to build our CMake project and setup our python wrappers.
if(SKBUILD)
    MESSAGE(STATUS "Trying to build using scikit-build")
    EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} -c "import importlib.resources; print(importlib.resources.files('skbuild').joinpath('resources/cmake'), end='')" OUTPUT_VARIABLE PYTHON_SKLIB_CMAKE_DIR)
    MESSAGE(STATUS "The Python scikit-build CMake directory is: ${PYTHON_SKLIB_CMAKE_DIR}")
    set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PYTHON_SKLIB_CMAKE_DIR}/")
    #    find_package(PythonExtensions REQUIRED)
else()
    MESSAGE(STATUS "Could not find scikit-build for building.")
endif()


FIND_PACKAGE(Python3)

# We get the python libraries for our wrappers.
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/")
find_package(PythonLibs REQUIRED)
# We will include and link to all the targets henceforth.
include_directories(${PYTHON_INCLUDE_DIRS})
link_libraries(${PYTHON_LIBRARIES})

function(add_all_python_tests)
    file(GLOB_RECURSE python_files *.py)
#    list(REMOVE_ITEM python_files ${CMAKE_CURRENT_SOURCE_DIR}/__init__.py)
    list(TRANSFORM python_files REPLACE "${CMAKE_CURRENT_SOURCE_DIR}/" "" OUTPUT_VARIABLE python_files_relative)
    message(DEBUG "The python files relative to the current cmake execution is: ${python_files_relative}")
    message(DEBUG "Possibly ignoring the file: ${CMAKE_CURRENT_SOURCE_DIR}/__init__.py")
    add_python_tests(${python_files_relative})
endfunction()

function(add_python_tests)
    foreach(python_file IN LISTS ARGN)
        add_python_test(${python_file})
    endforeach()
endfunction()

function(add_python_test python_file)
    find_package(Python COMPONENTS Interpreter REQUIRED)
    STRING(REGEX REPLACE "\.py$" "" test_name ${python_file})
    message(DEBUG "Trying to add the python tests from: ${python_file} (${CMAKE_CURRENT_SOURCE_DIR}/${python_file})")
    add_test(NAME ${test_name} COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${python_file})
endfunction()

function(install_python_target target destination)
    if(SKBUILD)
        find_package(PythonExtensions REQUIRED)
        include_directories(${PYTHON_INCLUDE_DIRS})
        target_link_libraries(${target} ${PYTHON_LIBRARIES})
        python_extension_module(${target})
        install(TARGETS ${target} LIBRARY DESTINATION ${destination})
    endif()
endfunction()

# Where we find the source files for our builds.
add_subdirectory(src)

