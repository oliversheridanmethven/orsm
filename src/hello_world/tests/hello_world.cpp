#include "hello_world/hello_world.hpp"
#include "testing/testing.hpp"

Test(hello_world, hello_world_to_stdout) {
    testing::internal::CaptureStdout();
    hello_world();
    ASSERT_EQ("Hello world.", testing::internal::GetCapturedStdout());
}
