/* An example of using the Criterion testing framework. */

# include "testing/testing.h"

/* This is what a failing test looks like. */
TEST(example, test_failure) {
    GTEST_SKIP();
    EXPECT_EQ(1, 2) << "This should fail.";
}

TEST(example, test_expect) {
    EXPECT_EQ(strlen("Hello"), 5) << "This should pass.";
}

TEST(example, test_fail) {
    ASSERT_EQ(2, 1 + 1) << "This should pass.";
    ASSERT_NE(1, 2) << "This should pass.";
}

TEST(logging, test_exit) {
    EXPECT_EXIT(exit(1), testing::ExitedWithCode(1), "") << "Should exit.";
}

