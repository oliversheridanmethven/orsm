#include "rubiks/shufflers/shufflers.hpp"
#include "rubiks/shapes/cube.hpp"
#include "rubiks/shapes/volume.hpp"
#include "testing/testing.h"

using namespace rubiks::shapes::cubics;
using namespace rubiks::shufflers;

template<typename S>
class ShapeShufflerTest : public testing::Test
{
};

using ShapeTypes = ::testing::Types<Volume, Cube>;
TYPED_TEST_SUITE(ShapeShufflerTest, ShapeTypes);

TYPED_TEST(ShapeShufflerTest, trivial_difficulty)
{
    TypeParam shape;
    auto turns = 0;
    auto seed = 0;
    auto [shuffled, shuffle_path] = specific(shape, turns, seed = 0);
    ASSERT_EQ(shuffled, shape);
    ASSERT_EQ(shuffle_path.size(), turns);
}

TYPED_TEST(ShapeShufflerTest, easy_difficulty)
{
    TypeParam shape;
    auto seed = 0;
    for (auto turns: {1, 2})
    {
        auto [shuffled, shuffle_path] = specific(shape, turns, seed);
        ASSERT_NE(shuffled, shape);
        ASSERT_EQ(shuffle_path.size(), turns);
    }
}

TYPED_TEST(ShapeShufflerTest, moderate_difficulty)
{
    TypeParam shape;
    auto seed = 0;
    for (auto turns = 1; turns < 5; turns++)
    {
        auto [shuffled, shuffle_path] = specific(shape, turns, seed);
        ASSERT_NE(shuffled, shape);
        ASSERT_EQ(shuffle_path.size(), turns);
    }
}

TYPED_TEST(ShapeShufflerTest, infeasible_moderate_difficulty)
{
    GTEST_SKIP(); /* This takes too long. */
    TypeParam shape;
    auto turns = 50;
    auto seed = 0;
    ASSERT_THROW(specific(shape, turns, seed), std::runtime_error)
            << "We should not have been able to produce a difficulty this large.";
}

TYPED_TEST(ShapeShufflerTest, moderate_god_shuffle)
{
    GTEST_SKIP(); /* This takes too long. */
    TypeParam shape;
    auto seed = 0;
    auto [shuffled, shuffle_path] = god(shape, seed);
    if (std::is_same<TypeParam, Volume>::value)
    {
        ASSERT_EQ(shuffle_path.size(), 11)
                << "We did not recover the god shuffle quoted in: cf: https://ruwix.com/the-rubiks-cube/gods-number/";
    }
    else if (std::is_same<TypeParam, Cube>::value)
    {
        /* For a regular cube whose faces can move (and the centres stay fixed) the god number is known to be 20.
         * However, we allow more degrees of freedom and the centres to move, so our god number should be less. However,
         * in lieu of know what is should be for our specification, then we will guess 20 until we ever actually
         * run this test. */
        ASSERT_EQ(shuffle_path.size(), 20)
                << "We did not recover the god shuffle quoted in: cf: https://ruwix.com/the-rubiks-cube/gods-number/";
    }
}
