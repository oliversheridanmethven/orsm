#include <stdio.h>
#include <stdbool.h>
#include <argp.h>
#include "version.h"

static int parse_opt (int key, char *arg, struct argp_state *state)
{
 switch (key)
 {
 case 'f':
 {
 printf("Doing something");
 break;
 }
 }
 return 0;
}


struct arguments {
    enum { CHARACTER_MODE, WORD_MODE, LINE_MODE } mode;
    bool isCaseInsensitive;
};

const char *argp_program_version = REPO_NAME " " REPO_VERSION;
const char *argp_program_bug_address = REPO_AUTHOR " <" REPO_EMAIL ">";
static char doc[] = "A small program to demonstrate using the command line interface.";

int main (int argc, char **argv)
{
    struct arguments arguments;
    arguments.mode = CHARACTER_MODE;
    arguments.isCaseInsensitive = false;

 struct argp_option options[] =
 {
 { "foo", 'f', 0, 0, "Do something perhaps."},
 { 0 }
 };
 struct argp argp = { options, parse_opt, 0, doc};
 return argp_parse (&argp, argc, argv, 0, 0, &arguments);
}