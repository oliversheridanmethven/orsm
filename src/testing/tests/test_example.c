/* An example of using the Criterion testing framework. */

#include <string.h>
#include "testing.h"

/* This is what a failing test looks like. */
//Test(example, test_failure) {
//    cr_expect(strlen("Hello") == 4, "This should fail.");
//}

Test(example, test_pass) {
    EXPECT(strlen("Hello") == 5, "This should pass.");
}