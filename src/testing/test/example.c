/* An example of using the Criterion testing framework. */

#include "testing/testing.h"
#include <string.h>

/* This is what a failing test looks like. */
//Test(example, test_failure) {
//    cr_expect(eq(int,1,2), "This should fail.");
//}

Test(example, test_expect)
{
    cr_expect(strlen("Hello") == 5, "This should pass.");
}

Test(example, test_fail)
{
    cr_assert(eq(int, 2, 1 + 1), "This should pass.");
    cr_assert(not(eq(int, 1, 2)), "This should pass.");
}

Test(logging, test_exit, .exit_code = 1)
{
    exit(1);// This terminates the program.
}
