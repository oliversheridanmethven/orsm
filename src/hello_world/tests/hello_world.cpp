#include "hello_world/hello_world.hpp"
#include "testing/testing.h"

/* Taken from: https://stackoverflow.com/a/58369622/5134817. */
class CaptureStdOutFixture : public ::testing::Test {
protected:
    CaptureStdOutFixture() : sbuf{nullptr} {
        // intentionally empty
    }

    ~CaptureStdOutFixture() override = default;

    // Called before each unit test
    void SetUp() override {
        // Save cout's buffer...
        sbuf = std::cout.rdbuf();
        // Redirect cout to our stringstream buffer or any other ostream
        std::cout.rdbuf(buffer.rdbuf());
    }

    // Called after each unit test
    void TearDown() override {
        // When done redirect cout to its old self
        std::cout.rdbuf(sbuf);
        sbuf = nullptr;
    }

    // The following objects can be reused in each unit test

    // This can be an ofstream as well or any other ostream
    std::stringstream buffer{};
    // Save cout's buffer here
    std::streambuf *sbuf;
};


TEST_F(CaptureStdOutFixture, hello_world_to_stdout) {
    hello_world();
    std::string captured_output{buffer.str()};
    ASSERT_EQ("Hello world.\n", captured_output);
}
