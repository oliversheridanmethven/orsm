#ifndef CLI_TESTING_H_
#define CLI_TESTING_H_

#include "logging/logging.h"
#include "testing/testing.h"
#include <argp.h>
#include <stdio.h>
#include <wordexp.h>

wordexp_t words;

struct arguments {
    enum
    {
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

void initialise_params(char *args)
{
    LOG_INFO("Parsing the input string: %s", args);
    char *command_prefix = "command ";
    char *merged = malloc(strlen(command_prefix) + strlen(args) + 1);
    if (!merged)
    {
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
    params.arguments.mode = CHARACTER_MODE;
    params.arguments.isCaseInsensitive = false;
}

void finalise_params(void)
{
    wordfree(&words);
}

TestSuite(cli, .init = show_all_logging, .fini = finalise_params);

#endif /*CLI_TESTING_H_*/