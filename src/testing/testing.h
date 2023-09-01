#ifndef TESTING_HPP_
#define TESTING_HPP_

#include <criterion/criterion.h>
#include <criterion/new/assert.h>
#include <criterion/redirect.h>

void redirect_all_stdout(void) {
    cr_redirect_stdout();
    setbuf(stdout, NULL);
    cr_redirect_stderr();
    setbuf(stderr, NULL);
}

#endif /*TESTING_HPP_*/
