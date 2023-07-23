#include "cli_testing.h"

Test(cli, nothing) {
    initialise_params("");
    argp_parse(0, params.argc, params.argv, 0, 0, 0);
}

Test(cli, help) {
    initialise_params("--help");
    argp_parse(0, params.argc, params.argv, 0, 0, 0);
}

Test(cli, usage) {
    initialise_params("--usage");
    argp_parse(0, params.argc, params.argv, 0, 0, 0);
}

Test(cli, extra_flag) {
    initialise_params("--foo");
    cr_assert(ne(int, 0, argp_parse(0, params.argc, params.argv, ARGP_NO_EXIT, 0, 0)), "This shouldn't have parsed a flag which doesn't exist.");
}

Test(cli, case_sensitive) {
    initialise_params("--Help");
    cr_assert(ne(int, 0, argp_parse(0, params.argc, params.argv, ARGP_NO_EXIT, 0, &params.arguments)), "This should be case sensitive.");
}

