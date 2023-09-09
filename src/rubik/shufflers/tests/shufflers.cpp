#include "testing/testing.h"
#include "rubik/shapes/volume.hpp"
#include "rubik/shufflers/shufflers.hpp"


template<typename S>
class ShapeShufflerTest : public testing::Test {
};

using ShapeTypes = ::testing::Types<Volume>;
TYPED_TEST_SUITE(ShapeShufflerTest, ShapeTypes);

TYPED_TEST(ShapeShufflerTest, trivial_difficulty) {
    TypeParam shape;
    auto turns = 0;
    auto seed = 0;
    auto [shuffled, shuffle_path] = specific(shape, turns, seed = 0);
    ASSERT_EQ(shuffled, shape);
    ASSERT_EQ(shuffle_path.size(), turns);
}

TYPED_TEST(ShapeShufflerTest, easy_difficulty) {
    TypeParam shape;
    auto seed = 0;
    for (auto turns: {1, 2}) {
        auto [shuffled, shuffle_path] = specific(shape, turns, seed);
        ASSERT_NE(shuffled, shape);
        ASSERT_EQ(shuffle_path.size(), turns);
    }
}

TYPED_TEST(ShapeShufflerTest, moderate_difficulty) {
    TypeParam shape;
    auto seed = 0;
    for (auto turns = 1; turns < 5; turns++) {
        auto [shuffled, shuffle_path] = specific(shape, turns, seed);
        ASSERT_NE(shuffled, shape);
        ASSERT_EQ(shuffle_path.size(), turns);
    }
}

TEST(ShufflerTest, infeasible_moderate_difficulty) {
    GTEST_SKIP(); /* This takes too long. */
    Volume shape;
    auto turns = 20;
    auto seed = 0;
    ASSERT_THROW(specific(shape, turns, seed), std::runtime_error)
                                << "We should not have been able to produce a difficulty this large.";
}

TEST(ShufflerTest, moderate_god_shuffle) {
    GTEST_SKIP(); /* This takes too long. */
    Volume shape;
    auto seed = 0;
    auto [shuffled, shuffle_path] = god(shape, seed);
    ASSERT_EQ(shuffle_path.size(), 11)
                                << "We did not recover the god shuffle quoted in: cf: https://ruwix.com/the-rubiks-cube/gods-number/";
}

