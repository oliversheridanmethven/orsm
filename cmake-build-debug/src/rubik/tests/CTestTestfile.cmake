# CMake generated Testfile for 
# Source directory: /Users/oliver/ClionProjects/testing/src/rubik/tests
# Build directory: /Users/oliver/ClionProjects/testing/cmake-build-debug/src/rubik/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[shape]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/rubik/tests/shape.py")
set_tests_properties([=[shape]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;129;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;122;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;117;add_python_tests;/Users/oliver/ClionProjects/testing/src/rubik/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/rubik/tests/CMakeLists.txt;0;")
add_test([=[solvers]=] "/Users/oliver/ClionProjects/testing/venv/bin/python3.11" "/Users/oliver/ClionProjects/testing/src/rubik/tests/solvers.py")
set_tests_properties([=[solvers]=] PROPERTIES  ENVIRONMENT "PYTHONPATH=/Users/oliver/ClionProjects/testing/src:" _BACKTRACE_TRIPLES "/Users/oliver/ClionProjects/testing/CMakeLists.txt;129;add_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;122;add_python_test;/Users/oliver/ClionProjects/testing/CMakeLists.txt;117;add_python_tests;/Users/oliver/ClionProjects/testing/src/rubik/tests/CMakeLists.txt;1;add_all_python_tests;/Users/oliver/ClionProjects/testing/src/rubik/tests/CMakeLists.txt;0;")
