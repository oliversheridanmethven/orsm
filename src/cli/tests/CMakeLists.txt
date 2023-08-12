# To add the command line argument parser.
# We follow several of the examples from:
# https://www.gnu.org/software/libc/manual/html_node/Argp-Examples.html
# http://nongnu.askapache.com/argpbook/step-by-step-into-argp.pdf
set(DEPS argp testing logging version)
add_executable(cli_arguments_0 cli_arguments_0.c)
target_link_libraries(cli_arguments_0 ${DEPS})
add_test(NAME cli_arguments_0 COMMAND cli_arguments_0)
add_executable(cli_arguments_version cli_arguments_version.c)
target_link_libraries(cli_arguments_version ${DEPS})
add_test(NAME cli_arguments_version COMMAND cli_arguments_version)