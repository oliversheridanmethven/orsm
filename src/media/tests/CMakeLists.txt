add_all_python_tests()
# The window test has some assertions on producing frame rates fast enough, so requires
# that it is not competing for CPU resources, so we give it some cores exclusively.
set_tests_properties(window PROPERTIES PROCESSOR_AFFINITY ON PROCESSORS ${N_CORES})
