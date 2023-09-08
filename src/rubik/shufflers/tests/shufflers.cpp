#include "testing/testing.h"
#include "rubik/shapes/volume.hpp"


template<typename S>
class ShapeShufflerTest : public testing::Test {
};

using ShapeTypes = ::testing::Types<Volume>;
TYPED_TEST_SUITE(ShapeShufflerTest, ShapeTypes);

TYPED_TEST(ShapeShufflerTest, trivial_difficulty) {
    ASSERT_FALSE(true);
}
