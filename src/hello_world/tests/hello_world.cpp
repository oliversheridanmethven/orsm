#include "hello_world/hello_world.hpp"
#include "testing/testing.h"

TEST_F(CaptureStdOut, hello_world_to_stdout) {
    hello_world();
    ASSERT_EQ("Hello world.\n", captured_cout.str());
}
