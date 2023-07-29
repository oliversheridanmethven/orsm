#ifndef TESTING_H_
#define TESTING_H_

#include <criterion/criterion.h>
#include <criterion/new/assert.h>
#include <criterion/redirect.h>

void redirect_all_stdout(void)
{
    cr_redirect_stdout();
    setbuf(stdout, NULL);
    cr_redirect_stderr();
}

#endif /*TESTING_H_*/
