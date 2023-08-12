#include "hello_world/hello_world.h"
#include "testing/testing.h"
#include <stdio.h>
#include <unistd.h>

TestSuite(hello_world_test, .init = redirect_all_stdout);

Test(hello_world_test, hello_world_to_stdout) {
    hello_world();
    cr_assert_stdout_eq_str("Hello world.");
}
