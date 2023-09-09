find_package(Boost REQUIRED program_options)
link_directories(${Boost_LIBRARY_DIR})

add_executable(misc misc.cpp)
target_link_libraries(misc common)

