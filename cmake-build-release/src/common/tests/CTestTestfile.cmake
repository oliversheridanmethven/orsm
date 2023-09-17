# CMake generated Testfile for 
# Source directory: /Users/oliver/ClionProjects/testing/src/common/tests
# Build directory: /Users/oliver/ClionProjects/testing/cmake-build-release/src/common/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[arguments]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/arguments.py")
set_tests_properties([=[arguments]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[cli_print_logs]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/cli_print_logs.py")
set_tests_properties([=[cli_print_logs]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[logger]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/logger.py")
set_tests_properties([=[logger]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[output]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/output.py")
set_tests_properties([=[output]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[output_suppressor_c_extension]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/output_suppressor_c_extension.py")
set_tests_properties([=[output_suppressor_c_extension]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[timing]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/timing.py")
set_tests_properties([=[timing]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[variables]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/common/tests/variables.py")
set_tests_properties([=[variables]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;156;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;149;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;144;add_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
add_test([=[output_suppression]=] "/Users/oliver/ClionProjects/testing/src/common/tests/output_suppressor_c_extension.sh" "/Users/oliver/ClionProjects/testing/src/common/tests/output_suppressor_c_extension.py" "--suppress_output")
set_tests_properties([=[output_suppression]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;3;add_test;/Users/oliver/ClionProjects/testing/src/common/tests/CMakeLists.txt;0;")
