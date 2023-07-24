# A basic hello world.
add_library(hello_world_c SHARED hello_world.c)

# Adding the Python libraries.
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
target_link_libraries(hello_world_c ${PYTHON_LIBRARIES})

# Copy the __init__.py file
configure_file(__init__.py ${CMAKE_CURRENT_BINARY_DIR}/__init__.py COPYONLY)
configure_file(setup.py ${CMAKE_CURRENT_BINARY_DIR}/setup.py COPYONLY)


# Suppress prefix "lib" because Python does not allow this prefix
#set_target_properties(hello_world_c PROPERTIES PREFIX "")

set(PYTHON_INSTALL_PATH ${CMAKE_CURRENT_BINARY_DIR})
message("The python install path is: ${PYTHON_INSTALL_PATH}")
install(TARGETS hello_world_c #[[__init__.py]] DESTINATION "${PYTHON_INSTALL_PATH}")
