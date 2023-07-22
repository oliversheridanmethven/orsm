# To add the command line argument parser.
# We follow several of the examples from:
# https://www.gnu.org/software/libc/manual/html_node/Argp-Examples.html
# http://nongnu.askapache.com/argpbook/step-by-step-into-argp.pdf
add_executable(cli_arguments_0 cli_arguments_0.c)
target_link_libraries(cli_arguments_0 PRIVATE argp)
#target_link_libraries(cli_arguments_version PRIVATE argp)