#ifndef TESTING_CUBE_HPP
#define TESTING_CUBE_HPP

#include "rubiks/colours/colour_palette.hpp"
#include "rubiks/shapes/shape.hpp"
#include "rubiks/shapes/utils/printing_cubic_shapes.hpp"
#include <sstream>

namespace rubiks
{
    namespace shapes
    {
        namespace cubics
        {

            class Cube : public Shape<Cube, 3>
            {
            private:
                using Row = std::array<Tile, 3>;
                using Face = std::array<Row, 3>;
                using Faces = std::array<Face, 6>;

                static const Move move_1, move_2, move_3,
                        move_4, move_5, move_6,
                        move_7, move_8, move_9,
                        move_10, move_11, move_12,
                        move_13, move_14, move_15,
                        move_16, move_17, move_18,
                        move_19, move_20, move_21,
                        move_22, move_23, move_24,
                        move_25, move_26, move_27;

                consteval static std::array<int, 10> foo(void)
                {
                    std::array<int, 10> v;
                    for (size_t i = 0; i < 10; i++)
                    {
                        v.at(i) = i;
                    }
                    return v;
                }

            public:
                ~Cube() override {}

                Cube()
                {
                    //        tiles = starting_tiles;
                    // Equivalent to the following:
                    for (size_t t = 0; const auto &face: solved_faces())
                    {
                        for (const auto &row: face)
                        {
                            for (const auto &tile: row)
                            {
                                tiles.at(t++) = tile;
                            }
                        }
                    }
                }

                const std::vector<std::array<size_t, 3>> invariant_tile_positions(void) const override final
                {
                    return {{0, 0, 0},
                            {4, 2, 0},
                            {3, 0, 2}};
                }

                const std::vector<Move> moves(void) const override final
                {
                    return {move_1, move_2, move_3,
                            move_4, move_5, move_6,
                            move_7, move_8, move_9,
                            move_10, move_11, move_12,
                            move_13, move_14, move_15,
                            move_16, move_17, move_18,
                            move_19, move_20, move_21,
                            move_22, move_23, move_24,
                            move_25, move_26, move_27};
                }

                const std::unordered_map<Move, Move> reverse_moves(void) const override final
                {
                    return {{move_1, move_3},
                            {move_2, move_2},
                            {move_3, move_1},
                            {move_4, move_6},
                            {move_5, move_5},
                            {move_6, move_4},
                            {move_7, move_9},
                            {move_8, move_8},
                            {move_9, move_7},
                            {move_10, move_12},
                            {move_11, move_11},
                            {move_12, move_10},
                            {move_13, move_15},
                            {move_14, move_14},
                            {move_15, move_13},
                            {move_16, move_18},
                            {move_17, move_17},
                            {move_18, move_16},
                            {move_19, move_21},
                            {move_20, move_20},
                            {move_21, move_19},
                            {move_22, move_24},
                            {move_23, move_23},
                            {move_24, move_22},
                            {move_25, move_27},
                            {move_26, move_26},
                            {move_27, move_25}};
                }

                const std::vector<std::unordered_set<Move>> commutative_moves(void) const override final
                {
                    return {{move_1, move_2, move_3,
                             move_4, move_5, move_6,
                             move_7, move_8, move_9},
                            {move_10, move_11, move_12,
                             move_13, move_14, move_15,
                             move_16, move_17, move_18},
                            {move_19, move_20, move_21,
                             move_22, move_23, move_24,
                             move_25, move_26, move_27},
                            {move_2, move_11, move_20}};
                }

                friend std::ostream &operator<<(std::ostream &os, const Cube &cube)
                {
                    os << cubics::internal::to_string(cube.faces(), ColourPalette());
                    return os;
                }
            };

            const Move
                    Cube::move_1 = {
                            "Move the second bottom (front -> right).",
                            {0, 1, 2, 30, 31, 32, 6, 7, 8, 9, 10, 11, 21, 22, 23, 15, 16, 17, 18, 19, 20, 3, 4, 5, 24, 25, 26,
                             27,
                             28, 29,
                             12, 13, 14, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53}},
                    Cube::move_2 = {"Move the second bottom (front -> back).", {0, 1, 2, 12, 13, 14, 6, 7, 8, 9, 10, 11, 3, 4, 5, 15, 16, 17, 18, 19, 20, 30, 31, 32, 24, 25, 26, 27, 28, 29, 21, 22, 23, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53}}, Cube::move_3 = {"Move the second bottom (front -> left).", {0, 1, 2, 21, 22, 23, 6, 7, 8, 9, 10, 11, 30, 31, 32, 15, 16, 17, 18, 19, 20, 12, 13, 14, 24, 25, 26, 27, 28, 29, 3, 4, 5, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53}}, Cube::move_4 = {"Move the first bottom (front -> right).", {0, 1, 2, 3, 4, 5, 33, 34, 35, 9, 10, 11, 12, 13, 14, 24, 25, 26, 18, 19, 20, 21, 22, 23, 6, 7, 8, 27, 28, 29, 30, 31, 32, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 48, 45, 52, 49, 46, 53, 50, 47}}, Cube::move_5 = {"Move the first bottom (front -> back).", {0, 1, 2, 3, 4, 5, 15, 16, 17, 9, 10, 11, 12, 13, 14, 6, 7, 8, 18, 19, 20, 21, 22, 23, 33, 34, 35, 27, 28, 29, 30, 31, 32, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 53, 52, 51, 50, 49, 48, 47, 46, 45}}, Cube::move_6 = {"Move the first bottom (front -> left).", {0, 1, 2, 3, 4, 5, 24, 25, 26, 9, 10, 11, 12, 13, 14, 33, 34, 35, 18, 19, 20, 21, 22, 23, 15, 16, 17, 27, 28, 29, 30, 31, 32, 6, 7, 8, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 50, 53, 46, 49, 52, 45, 48, 51}}, Cube::move_7 = {"Move all the bottom (front -> right).", {0, 1, 2, 30, 31, 32, 33, 34, 35, 9, 10, 11, 21, 22, 23, 24, 25, 26, 18, 19, 20, 3, 4, 5, 6, 7, 8, 27, 28, 29, 12, 13, 14, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 48, 45, 52, 49, 46, 53, 50, 47}}, Cube::move_8 = {"Move all the bottom (front -> back).", {0, 1, 2, 12, 13, 14, 15, 16, 17, 9, 10, 11, 3, 4, 5, 6, 7, 8, 18, 19, 20, 30, 31, 32, 33, 34, 35, 27, 28, 29, 21, 22, 23, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 53, 52, 51, 50, 49, 48, 47, 46, 45}}, Cube::move_9 = {"Move all the bottom (front -> left).", {0, 1, 2, 21, 22, 23, 24, 25, 26, 9, 10, 11, 30, 31, 32, 33, 34, 35, 18, 19, 20, 12, 13, 14, 15, 16, 17, 27, 28, 29, 3, 4, 5, 6, 7, 8, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 50, 53, 46, 49, 52, 45, 48, 51}}, Cube::move_10 = {"Move the second right (front -> top).", {0, 46, 2, 3, 49, 5, 6, 52, 8, 9, 43, 11, 12, 40, 14, 15, 37, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 1, 38, 39, 4, 41, 42, 7, 44, 45, 16, 47, 48, 13, 50, 51, 10, 53}}, Cube::move_11 = {"Move the second right (front -> back).", {0, 16, 2, 3, 13, 5, 6, 10, 8, 9, 7, 11, 12, 4, 14, 15, 1, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 46, 38, 39, 49, 41, 42, 52, 44, 45, 37, 47, 48, 40, 50, 51, 43, 53}}, Cube::move_12 = {"Move the second right (front -> bottom).", {0, 37, 2, 3, 40, 5, 6, 43, 8, 9, 52, 11, 12, 49, 14, 15, 46, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 16, 38, 39, 13, 41, 42, 10, 44, 45, 1, 47, 48, 4, 50, 51, 7, 53}}, Cube::move_13 = {"Move the first right (front -> top).", {0, 1, 47, 3, 4, 50, 6, 7, 53, 44, 10, 11, 41, 13, 14, 38, 16, 17, 24, 21, 18, 25, 22, 19, 26, 23, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 2, 39, 40, 5, 42, 43, 8, 45, 46, 15, 48, 49, 12, 51, 52, 9}}, Cube::move_14 = {"Move the first right (front -> back).", {0, 1, 15, 3, 4, 12, 6, 7, 9, 8, 10, 11, 5, 13, 14, 2, 16, 17, 26, 25, 24, 23, 22, 21, 20, 19, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 47, 39, 40, 50, 42, 43, 53, 45, 46, 38, 48, 49, 41, 51, 52, 44}}, Cube::move_15 = {"Move the first right (front -> bottom).", {0, 1, 38, 3, 4, 41, 6, 7, 44, 53, 10, 11, 50, 13, 14, 47, 16, 17, 20, 23, 26, 19, 22, 25, 18, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 15, 39, 40, 12, 42, 43, 9, 45, 46, 2, 48, 49, 5, 51, 52, 8}}, Cube::move_16 = {"Move all the right (front -> top).", {0, 46, 47, 3, 49, 50, 6, 52, 53, 44, 43, 11, 41, 40, 14, 38, 37, 17, 24, 21, 18, 25, 22, 19, 26, 23, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 1, 2, 39, 4, 5, 42, 7, 8, 45, 16, 15, 48, 13, 12, 51, 10, 9}}, Cube::move_17 = {"Move all the right (front -> back).", {0, 16, 15, 3, 13, 12, 6, 10, 9, 8, 7, 11, 5, 4, 14, 2, 1, 17, 26, 25, 24, 23, 22, 21, 20, 19, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 46, 47, 39, 49, 50, 42, 52, 53, 45, 37, 38, 48, 40, 41, 51, 43, 44}}, Cube::move_18 = {"Move all the right (front -> bottom).", {0, 37, 38, 3, 40, 41, 6, 43, 44, 53, 52, 11, 50, 49, 14, 47, 46, 17, 20, 23, 26, 19, 22, 25, 18, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 16, 15, 39, 13, 12, 42, 10, 9, 45, 1, 2, 48, 4, 5, 51, 7, 8}}, Cube::move_19 = {"Move the second back (top -> left).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 50, 20, 21, 49, 23, 24, 48, 26, 27, 41, 29, 30, 40, 32, 33, 39, 35, 36, 37, 38, 19, 22, 25, 42, 43, 44, 45, 46, 47, 28, 31, 34, 51, 52, 53}}, Cube::move_20 = {"Move the second back (top -> bottom).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 34, 20, 21, 31, 23, 24, 28, 26, 27, 25, 29, 30, 22, 32, 33, 19, 35, 36, 37, 38, 50, 49, 48, 42, 43, 44, 45, 46, 47, 41, 40, 39, 51, 52, 53}}, Cube::move_21 = {"Move the second back (top -> right).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 39, 20, 21, 40, 23, 24, 41, 26, 27, 48, 29, 30, 49, 32, 33, 50, 35, 36, 37, 38, 34, 31, 28, 42, 43, 44, 45, 46, 47, 25, 22, 19, 51, 52, 53}}, Cube::move_22 = {"Move the first back (top -> left).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 18, 19, 53, 21, 22, 52, 24, 25, 51, 38, 28, 29, 37, 31, 32, 36, 34, 35, 20, 23, 26, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 27, 30, 33}}, Cube::move_23 = {"Move the first back (top -> bottom).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9, 18, 19, 33, 21, 22, 30, 24, 25, 27, 26, 28, 29, 23, 31, 32, 20, 34, 35, 53, 52, 51, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 38, 37, 36}}, Cube::move_24 = {"Move the first back (top -> right).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 17, 10, 13, 16, 9, 12, 15, 18, 19, 36, 21, 22, 37, 24, 25, 38, 51, 28, 29, 52, 31, 32, 53, 34, 35, 33, 30, 27, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 26, 23, 20}}, Cube::move_25 = {"Move all the back (top -> left).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 18, 50, 53, 21, 49, 52, 24, 48, 51, 38, 41, 29, 37, 40, 32, 36, 39, 35, 20, 23, 26, 19, 22, 25, 42, 43, 44, 45, 46, 47, 28, 31, 34, 27, 30, 33}}, Cube::move_26 = {"Move all the back (top -> bottom).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9, 18, 34, 33, 21, 31, 30, 24, 28, 27, 26, 25, 29, 23, 22, 32, 20, 19, 35, 53, 52, 51, 50, 49, 48, 42, 43, 44, 45, 46, 47, 41, 40, 39, 38, 37, 36}}, Cube::move_27 = {"Move all the back (top -> right).", {0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 17, 10, 13, 16, 9, 12, 15, 18, 39, 36, 21, 40, 37, 24, 41, 38, 51, 48, 29, 52, 49, 32, 53, 50, 35, 33, 30, 27, 34, 31, 28, 42, 43, 44, 45, 46, 47, 25, 22, 19, 26, 23, 20}};

        }// namespace cubics
    }    // namespace shapes
}// namespace rubiks

#endif//TESTING_CUBE_HPP
