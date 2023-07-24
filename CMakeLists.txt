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
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${ERROR_FLAGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${ERROR_FLAGS}")



include(CheckCCompilerFlag)
CHECK_C_COMPILER_FLAG("-std=c2x" COMPILER_SUPPORTS_C2X)
if(COMPILER_SUPPORTS_C2X)
    message(STATUS "Compiler ${CMAKE_C_COMPILER} appears to have C2X support.")
#    foreach(i ${CMAKE_C_COMPILE_FEATURES})
#        message("${i}")
#    endforeach()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c2x")
else()
    message(FATAL_ERROR "Compiler ${CMAKE_C_COMPILER} has no C2X support.")
endif()

# To enable testing and use of ctest.
enable_testing()
# ^ This must be before any calls to add_subdirectory to ensure it is enabled recursively.
# cf. https://stackoverflow.com/questions/54550939/ctest-add-tests-in-subdirectories#comment109191766_55835742





# Some C++ examples.
#add_executable(main main.cpp my_stacks.hpp my_queues.hpp my_minimum.hpp) # my_sort.hpp my_sort.cpp)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/")
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})


function(install_python_target target destination)
    if(SKBUILD)
        find_package(PythonExtensions REQUIRED)
        include_directories(${PYTHON_INCLUDE_DIRS})
        target_link_libraries(${target} ${PYTHON_LIBRARIES})
        python_extension_module(${target})
        install(TARGETS ${target} LIBRARY DESTINATION ${destination})
    endif()
endfunction()

# We use scikit-build to our python wrappers.
if(SKBUILD)
    MESSAGE(STATUS "Trying to build using scikit-build")
    EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} -c "import importlib.resources; print(importlib.resources.files('skbuild').joinpath('resources/cmake'), end='')" OUTPUT_VARIABLE PYTHON_SKLIB_CMAKE_DIR)
    MESSAGE(STATUS "The Python scikit-build CMake directory is: ${PYTHON_SKLIB_CMAKE_DIR}")
    set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PYTHON_SKLIB_CMAKE_DIR}/")
#    find_package(PythonExtensions REQUIRED)
else()
    MESSAGE(STATUS "Could not find scikit-build for building.")
endif()



add_library(hello MODULE hello/hello.c)
install_python_target(hello hello)

add_subdirectory(foo)
#add_library(bar MODULE foo/bar/bar.c)
#install_python_target(bar bar)
# Where we find the source files for our builds.
add_subdirectory(src)


