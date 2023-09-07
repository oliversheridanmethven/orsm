#include "testing/testing.h"
#include "rubik/shapes/volume.hpp"

template<typename S>
class ShapeTest : public testing::Test {
};

using ShapeTypes = ::testing::Types<Volume>;
TYPED_TEST_SUITE(ShapeTest, ShapeTypes);

TYPED_TEST(ShapeTest, printing) {
    TypeParam shape;
    LOG_DEBUG << shape;
}

TYPED_TEST(ShapeTest, equality) {
    TypeParam shape1, shape2;
    ASSERT_EQ(shape1, shape2);
}

TYPED_TEST(ShapeTest, hashing) {
    TypeParam shape1, shape2;
    ASSERT_EQ(std::hash<TypeParam>{}(shape1), std::hash<TypeParam>{}(shape2));
}

TYPED_TEST(ShapeTest, moves_equality) {
    TypeParam shape;
    auto moves = shape.moves();
    for (size_t i = 0; i < moves.size(); i++) {
        for (size_t j = 0; j < moves.size(); j++) {
            if (i == j) {
                ASSERT_EQ(moves.at(i), moves.at(j));
            } else {
                ASSERT_NE(moves.at(i), moves.at(j));
            }
        }
    }
}

TYPED_TEST(ShapeTest, single_moves) {
    TypeParam shape1, shape2, shape3;
    for (auto move: shape1.moves()) {
        shape3 = shape2.move(move);
        ASSERT_NE(shape3, shape2);
        ASSERT_EQ(shape1, shape2);
    }
}




