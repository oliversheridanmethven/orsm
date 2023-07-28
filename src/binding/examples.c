#include "examples.h"
#include <stdio.h>
#include <stdlib.h>

void hello_world(void)
{
    int rc = puts("Hello world from within C.\n");
    if (rc == EOF || rc < 0)
    {
        exit(1);
    }
}

void foo(int a, char *b)
{
    int rc = printf("The input values are: a = %i and b = %s\n", a, b);
    if (rc < 0)
    {
        exit(1);
    }
}

void fatal_failure(void)
{
    fprintf(stderr, "We are fatally failing now.\n");
    exit(1);
}

void non_fatal_failure(void)
{
    fprintf(stderr, "We are non-fatally failing now.\n");
    exit(1);
}
