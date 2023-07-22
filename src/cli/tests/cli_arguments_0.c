#include <stdio.h>
#include <argp.h>
#include <wordexp.h>
#include "testing/testing.h"
#include "logging/logging.h"

wordexp_t words;

struct params {
    int argc;
    char ** argv;
} params;

void initialise_params(char * args) {
    LOG_INFO("Parsing the input string: %s", args);
    char *command_prefix = "command ";
    char *merged = malloc(strlen(command_prefix) + strlen(args) + 1);
    if (!merged) {
        LOG_ERROR("Couldn't allocate enough space for the command string.");
    }
    strcpy(merged, command_prefix);
    strcat(merged, args);
    args = merged;

    switch (wordexp(args, &words, 0))
    {
        case 0:
          LOG_INFO("Successfully parsed the input string: %s", args);
          break;
        default:
          LOG_ERROR("Failed trying to parse the input string: %s", args);
          break;
    }
    params.argc = words.we_wordc;
    params.argv = words.we_wordv;
}

void finalise_params(void) {
   wordfree(&words);
}

TestSuite(cli, .init=show_all_logging);

Test(cli, nothing, .fini=finalise_params) {
    initialise_params("");
    argp_parse(0, params.argc, params.argv, 0, 0, 0);
}

Test(cli, help, .fini=finalise_params) {
    initialise_params("--help");
    argp_parse(0, params.argc, params.argv, 0, 0, 0);
}

Test(cli, usage, .fini=finalise_params) {
    initialise_params("--usage");
    argp_parse(0, params.argc, params.argv, 0, 0, 0);
}

Test(cli, extra_flag, .fini=finalise_params) {
    initialise_params("--foo");
    cr_assert(ne(int, 0, argp_parse(0, params.argc, params.argv, ARGP_NO_EXIT, 0, 0)), "This shouldn't have parsed a flag which doesn't exist.");
}

