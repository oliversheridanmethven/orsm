#ifndef TESTING_VOLUME_HPP
#define TESTING_VOLUME_HPP

#include "rubik/shapes/shape.hpp"
#include "rubik/shapes/utils/printing_cubic_shapes.hpp"
#include "rubik/colours/colour_palette.hpp"
#include <sstream>

class Volume final : public Shape<Volume, 2> {
private:
    static const Move move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8, move_9;

public:
//    ~Volume() override {}

    /*
     * The CRTP pattern makes trying to code this up as an initialiser list awkward, but for now it's no the
     * bottleneck, so don't stress about it for now.
     *
     * */
    Tiles starting_tiles{ColourPalette::Colour::red, ColourPalette::Colour::red, ColourPalette::Colour::red,
                         ColourPalette::Colour::red, ColourPalette::Colour::yellow, ColourPalette::Colour::yellow,
                         ColourPalette::Colour::yellow, ColourPalette::Colour::yellow,
                         ColourPalette::Colour::blue,
                         ColourPalette::Colour::blue, ColourPalette::Colour::blue, ColourPalette::Colour::blue,
                         ColourPalette::Colour::green, ColourPalette::Colour::green, ColourPalette::Colour::green,
                         ColourPalette::Colour::green, ColourPalette::Colour::white, ColourPalette::Colour::white,
                         ColourPalette::Colour::white, ColourPalette::Colour::white,
                         ColourPalette::Colour::light_yellow,
                         ColourPalette::Colour::light_yellow, ColourPalette::Colour::light_yellow,
                         ColourPalette::Colour::light_yellow};

    Volume() {
        tiles = starting_tiles;
        // Equivalent to the following, but faster:
        /*
        for (auto face: solved_faces()) {
            for (auto row: face) {
                for (auto tile: row) {
                    tiles.push_back(tile);
                }
            }
        }
        */
    }


    const std::vector<Move> moves(void) const override final {
        return {move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8, move_9};
    }

    const std::unordered_map<Move, Move> reverse_moves(void) const override final {
        return {{move_1, move_3},
                {move_2, move_2},
                {move_3, move_1},
                {move_4, move_6},
                {move_5, move_5},
                {move_6, move_4},
                {move_7, move_9},
                {move_8, move_8},
                {move_9, move_7}};
    }

    const std::vector<std::unordered_set<Move>> commutative_moves(void) const override final {
        return {{move_1, move_2, move_3},
                {move_4, move_5, move_6},
                {move_7, move_8, move_9}
        };
    }


    friend std::ostream &operator<<(std::ostream &os, const Volume &volume) {
        os << cubic_shapes::to_string(volume.faces(), ColourPalette());
        return os;
    }

};

/* Must be defined outside the class because these are static to the class. */
const Move Volume::move_1 = {"Move the bottom (front -> right)",
                             {0, 1, 14, 15, 4, 5, 10, 11, 8, 9, 2, 3, 12, 13, 6, 7, 16, 17, 18, 19, 22, 20, 23,
                              21}},
        Volume::move_2 = {"Move the bottom (front -> back)",
                          {0, 1, 6, 7, 4, 5, 2, 3, 8, 9, 14, 15, 12, 13, 10, 11, 16, 17, 18, 19, 23, 22, 21, 20}},
        Volume::move_3 = {"Move the bottom (front -> left)",
                          {0, 1, 10, 11, 4, 5, 14, 15, 8, 9, 6, 7, 12, 13, 2, 3, 16, 17, 18, 19, 21, 23, 20, 22}},
        Volume::move_4 = {"Move the right (front -> top)",
                          {0, 21, 2, 23, 19, 5, 17, 7, 10, 8, 11, 9, 12, 13, 14, 15, 16, 1, 18, 3, 20, 6, 22, 4}},
        Volume::move_5 = {"Move the right (front -> back)",
                          {0, 6, 2, 4, 3, 5, 1, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16, 21, 18, 23, 20, 17, 22, 19}},
        Volume::move_6 = {"Move the right (front -> bottom)",
                          {0, 17, 2, 19, 23, 5, 21, 7, 9, 11, 8, 10, 12, 13, 14, 15, 16, 6, 18, 4, 20, 1, 22, 3}},
        Volume::move_7 = {"Move the back (top -> left)",
                          {0, 1, 2, 3, 6, 4, 7, 5, 8, 23, 10, 22, 17, 13, 16, 15, 9, 11, 18, 19, 20, 21, 12, 14}},
        Volume::move_8 = {"Move the back (top -> bottom)",
                          {0, 1, 2, 3, 7, 6, 5, 4, 8, 14, 10, 12, 11, 13, 9, 15, 23, 22, 18, 19, 20, 21, 17, 16}},
        Volume::move_9 = {"Move the back (top -> right)",
                          {0, 1, 2, 3, 5, 7, 4, 6, 8, 16, 10, 17, 22, 13, 23, 15, 14, 12, 18, 19, 20, 21, 11, 9}};


#endif //TESTING_VOLUME_HPP
