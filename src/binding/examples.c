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

void fail(void)
{
    fprintf(stderr, "We are failing now.\n");
    exit(1);
}
