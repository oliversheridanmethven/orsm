#include "testing/testing.h"
#include "common/suppressor/suppressor.h"
#include <stdio.h>

char *some_string;

void initialise_suppressor(void) {
    redirect_all_stdout();
    some_string = "Something";
    cr_assert_not(suppressing_start());
}

void finalise_suppressor(void) {
    cr_assert_not(suppressing_stop());
}

TestSuite(suppressor, .init=initialise_suppressor, .fini=finalise_suppressor);

Test(suppressor, redirect_stdout_puts) {
    puts(some_string);
    cr_assert_stdout_eq_str("");
    cr_assert_stdout_neq_str(some_string);
}

Test(suppressor, redirect_stdout_printf) {
    printf("%s", some_string);
    cr_assert_stdout_eq_str("");
    cr_assert_stdout_neq_str(some_string);
}

Test(suppressor, redirect_stderr) {
    fprintf(stderr, "%s", some_string);
    cr_assert_stderr_eq_str("");
    cr_assert_stderr_neq_str(some_string);
}
