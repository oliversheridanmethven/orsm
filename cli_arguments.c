#include <stdio.h>
#include <argp.h>
#include "version.h"

static int parse_opt (int key, char *arg, struct argp_state *state)
{
 switch (key)
 {
 case 'v':
 {
 printf("%s\n", REPO_VERSION);
 break;
 }
 }
 return 0;
}

int main (int argc, char **argv)
{
 struct argp_option options[] =
 {
 { "version", 'v', 0, 0, "The version number."},
 { 0 }
 };
 struct argp argp = { options, parse_opt, 0, 0 };
 return argp_parse (&argp, argc, argv, 0, 0, 0);
}