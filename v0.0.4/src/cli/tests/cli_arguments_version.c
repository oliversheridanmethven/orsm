#include "cli_testing.h"
#include "version/version.h"

const char *argp_program_version = REPO_NAME " " REPO_VERSION;
const char *argp_program_bug_address = REPO_AUTHOR " <" REPO_EMAIL ">";
static char doc[] = "A small program to demonstrate using the command line interface.";

Test(cli, test_version)
{
    initialise_params("--version");
    struct argp argp = {.doc = doc};
    argp_parse(&argp, params.argc, params.argv, 0, 0, &params.arguments);
}

static int parse_opt(int key, char *arg, struct argp_state *state)
{
    switch (key)
    {
        case 'f': {
            printf("Doing something");
            break;
        }
    }
    return 0;
}

Test(cli, test_short_option)
{
    initialise_params("--version");
    struct argp_option options[] =
            {
                    {"foo", 'f', 0, 0, "Do something perhaps."},
                    {0}};
    struct argp argp = {options, parse_opt};
    argp_parse(&argp, params.argc, params.argv, 0, 0, &params.arguments);
}
