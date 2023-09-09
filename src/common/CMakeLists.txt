add_subdirectory(tests)
add_subdirectory(suppressor)

find_package(Boost REQUIRED program_options filesystem)
add_library(common INTERFACE)
add_dependencies(common logging)
target_include_directories(common SYSTEM INTERFACE ${BOOST_INCLUDE_DIRS} )
target_include_directories(common INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)
target_link_libraries(common INTERFACE Boost::boost Boost::program_options Boost::filesystem version logging)


