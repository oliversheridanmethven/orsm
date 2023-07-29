add_all_python_tests()

add_test(output_suppression COMMAND ${BASH_PROGRAM} ${CMAKE_CURRENT_SOURCE_DIR}/output_suppressor_c_extension.sh ${CMAKE_CURRENT_SOURCE_DIR}/output_suppressor_c_extension.py --suppress_output)
