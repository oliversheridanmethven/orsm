#ifndef CLI_TESTING_H_
#define CLI_TESTING_H_

#include "logging/logging.h"
#include "testing/testing.h"
#include "version/version.h"
#include <argp.h>
#include <stdio.h>
#include <wordexp.h>

wordexp_t words;

struct arguments {
    enum {
        CHARACTER_MODE,
        WORD_MODE,
        LINE_MODE
    } mode;
    bool isCaseInsensitive;
};

struct params {
    int argc;
    char **argv;
    struct arguments arguments;
} params;

/* GNU argp required these be const, which we might remove occasionally. */
const char *argp_program_version = nullptr;
const char *argp_program_bug_address = nullptr;

void setup_program_details(void) {
    asprintf(&argp_program_version, "%s %s", repo_name(), repo_version());
    asprintf(&argp_program_bug_address, "%s <%s>", repo_author(), repo_email());
}

void clean_program_details(void) {
    free((char *) argp_program_version);
    free((char *) argp_program_bug_address);
}


void initialise_params(char *args) {
    LOG_INFO("Parsing the input string: %s", args);
    char *command_prefix = "command ";
    char *merged = malloc(strlen(command_prefix) + strlen(args) + 1);
    if (!merged) {
        LOG_ERROR("Couldn't allocate enough space for the command string.");
    }
    strcpy(merged, command_prefix);
    strcat(merged, args);
    args = merged;

    switch (wordexp(args, &words, 0)) {
        case 0:
            LOG_INFO("Successfully parsed the input string: %s", args);
            break;
        default:
            LOG_ERROR("Failed trying to parse the input string: %s", args);
            break;
    }
    params.argc = words.we_wordc;
    params.argv = words.we_wordv;
    params.arguments.mode = CHARACTER_MODE;
    params.arguments.isCaseInsensitive = false;
}

void finalise_params(void) {
    wordfree(&words);
}

void init_cli(void) {
    show_all_logging();
    setup_program_details();
}

void fini_cli(void) {
    finalise_params();
//    clean_program_details();
}

TestSuite(cli, .init = init_cli, .fini = fini_cli);

#endif /*CLI_TESTING_H_*/
