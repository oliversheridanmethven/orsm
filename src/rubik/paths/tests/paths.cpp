#include "testing/testing.h"
#include "rubik/paths/paths.hpp"
#include "rubik/shapes/volume.hpp"
#include <iostream>


TEST_F(CaptureStdOut, printing_empty) {
    Path path;
    std::cout << path;
    ASSERT_THAT(captured_cout.str(), ::testing::MatchesRegex("[Ee]mpty.*"));
}

TEST(Path, add) {
    Path path;
    ASSERT_TRUE(path.empty());
    Volume shape;
    auto move = shape.moves().front();

    auto added = path.add(move);
    ASSERT_TRUE(path.empty());
    ASSERT_FALSE(added.empty());
    ASSERT_NE(path, added);
    auto [ignore, reverse] = added.front();
    path.push_back({move, reverse});
    ASSERT_FALSE(path.empty());
    ASSERT_EQ(path, added);
}

TEST_F(CaptureStdOut, printing_nonempty) {
    Path path;
    Volume shape;
    path = path.add(shape.moves().front());
    std::cout << path;
    ASSERT_THAT(captured_cout.str(), Not(::testing::MatchesRegex("[Ee]mpty.*")));
}

TEST(Path, reversing_moves) {
    Path path;
    Volume shape;
    ASSERT_EQ(path.size(), 0);
    for (size_t path_length = 0; auto move: shape.moves()) {
        auto reversed = path.reversed();
        ASSERT_EQ(path.size(), reversed.size());
        for (auto [move_forward, forward]: path) {
            for (auto [move_reverse, reverse]: reversed) {
                CHECK_GE(path_length, 1);
                if (path_length == 1) {
                    ASSERT_EQ(move_forward, move_reverse);
                    ASSERT_NE(forward, reverse);
                } else {
                    ASSERT_NE(path, reversed);
                    auto only_reverted_directions = reversed;
                    std::ranges::reverse(only_reverted_directions);
                    // ^The order of the moves is reversed, but their direction stays the same.
                    ASSERT_NE(path, only_reverted_directions);
                    for (auto [_ignore, forward]: path) {
                        for (auto [_ignore, reverse]: only_reverted_directions) {
                            ASSERT_NE(forward,
                                      reverse) << "The Path.reversed() method should invert the directions, whereas std::ranges::reverse(Path) shouldn't.";
                        }
                    }
                }
            }
        }
        path = path.add(move);
        ASSERT_EQ(path.size(), ++path_length);
    }
}
