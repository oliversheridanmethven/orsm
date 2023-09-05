add_library(solvers meet_in_middle_recursive.cpp)
target_link_libraries(solvers paths shapes)

find_package(Boost REQUIRED program_options)
add_executable(demo_cpp demo.cpp)
target_link_libraries(demo_cpp logging colours paths solvers Boost::program_options)
