#ifndef TESTING_VOLUME_HPP
#define TESTING_VOLUME_HPP

#include "rubik/shapes/shape.hpp"
#include "rubik/colours/default_colours.hpp"
#include <sstream>
#include <boost/functional/hash.hpp>


const Move
        move_1 = {"Move the bottom (front -> right)",
                  {0, 1, 14, 15, 4, 5, 10, 11, 8, 9, 2, 3, 12, 13, 6, 7, 16, 17, 18, 19, 22, 20, 23, 21}},
        move_2 = {"Move the bottom (front -> back)",
                  {0, 1, 6, 7, 4, 5, 2, 3, 8, 9, 14, 15, 12, 13, 10, 11, 16, 17, 18, 19, 23, 22, 21, 20}},
        move_3 = {"Move the bottom (front -> left)",
                  {0, 1, 10, 11, 4, 5, 14, 15, 8, 9, 6, 7, 12, 13, 2, 3, 16, 17, 18, 19, 21, 23, 20, 22}},
        move_4 = {"Move the right (front -> top)",
                  {0, 21, 2, 23, 19, 5, 17, 7, 10, 8, 11, 9, 12, 13, 14, 15, 16, 1, 18, 3, 20, 6, 22, 4}},
        move_5 = {"Move the right (front -> back)",
                  {0, 6, 2, 4, 3, 5, 1, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16, 21, 18, 23, 20, 17, 22, 19}},
        move_6 = {"Move the right (front -> bottom)",
                  {0, 17, 2, 19, 23, 5, 21, 7, 9, 11, 8, 10, 12, 13, 14, 15, 16, 6, 18, 4, 20, 1, 22, 3}},
        move_7 = {"Move the back (top -> left)",
                  {0, 1, 2, 3, 6, 4, 7, 5, 8, 23, 10, 22, 17, 13, 16, 15, 9, 11, 18, 19, 20, 21, 12, 14}},
        move_8 = {"Move the back (top -> bottom)",
                  {0, 1, 2, 3, 7, 6, 5, 4, 8, 14, 10, 12, 11, 13, 9, 15, 23, 22, 18, 19, 20, 21, 17, 16}},
        move_9 = {"Move the back (top -> right)",
                  {0, 1, 2, 3, 5, 7, 4, 6, 8, 16, 10, 17, 22, 13, 23, 15, 14, 12, 18, 19, 20, 21, 11, 9}};


class Volume final : public Shape<Volume> {
private:

    Volume::Faces solved_faces(void) const {
        Faces faces;
        for (auto colour: ColourPalette().colours) {
            Face face;
            for (size_t i = 0; i < 2; i++) {
                Row row;
                for (size_t j = 0; j < 2; j++) {
                    row.push_back(colour);
                }
                face.push_back(row);
            }
            faces.push_back(face);
        }
        return faces;
    }

    virtual Volume::Faces faces(void) const override final {
        Faces faces = solved_faces();
        auto _tile = tiles.begin();
        for (auto &face: faces) {
            for (auto &row: face) {
                for (auto &tile: row) {
                    tile = *(_tile++);
                }
            }
        }
        return faces;
    }

public:

//    ~Volume() override {}

    Volume() {
        for (auto face: solved_faces()) {
            for (auto row: face) {
                for (auto tile: row) {
                    tiles.push_back(tile);
                }
            }
        }
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
        auto colour_palette = ColourPalette();
        auto faces = volume.faces();
        auto front = faces[0];
        auto back = faces[1];
        auto right = faces[2];
        auto left = faces[3];
        auto top = faces[4];
        auto bottom = faces[5];
        std::stringstream s, bars;
        s << "\n\n";
        size_t indent = 5;
        auto indenting = indent + 3;
        for (auto row: top) {
            for (size_t i = 0; i < indenting; i++) {
                s << ' ';
            }
            for (auto tile: row) {
                s << colour_palette.colour(std::to_string(colour_palette.value(tile.colour)), tile.colour) << " ";
            }
            s << '\n';
            indenting -= 1;
        }
        for (size_t i = 0; i < top[0].size() * 2; i++) {
            bars << '-';
        }
        for (size_t i = 0; i < indent; i++) { s << " "; }
        s << '/' << bars.str() << '/';
        for (size_t row = 0; row < left.size(); row++) {
            auto left_row = left[row],
                    front_row = front[row],
                    right_row = right[row],
                    back_row = back[row];
            s << "\n";

            for (auto tile: left_row) {
                s << colour_palette.colour(std::to_string(colour_palette.value(tile.colour)), tile.colour) << " ";
            }
            s << ": ";
            for (auto tile: front_row) {
                s << colour_palette.colour(std::to_string(colour_palette.value(tile.colour)), tile.colour) << " ";
            }
            s << ": ";
            for (auto tile: right_row) {
                s << colour_palette.colour(std::to_string(colour_palette.value(tile.colour)), tile.colour) << " ";
            }
            s << ": ";
            for (auto tile: back_row) {
                s << colour_palette.colour(std::to_string(colour_palette.value(tile.colour)), tile.colour) << " ";
            }
        }
        s << "\n";
        for (size_t i = 0; i < indent; i++) {
            s << " ";
        }
        s << "\\" << bars.str() << "\\";
        for (auto row: bottom) {
            s << '\n';
            indenting += 1;
            for (size_t i = 0; i < indenting; i++) {
                s << " ";
            }
            for (auto tile: row) {
                s << colour_palette.colour(std::to_string(colour_palette.value(tile.colour)), tile.colour) << " ";
            }
        }
        s << "\n\n";
        os << s.str();
        return os;
    }


    friend std::hash<Volume>;
};

//template<>
template<>
struct std::hash<Volume> {

    std::size_t operator()(const Volume &shape) const noexcept {
        size_t combined_hash = 0; /* <- Must be seeded. */
        for (const auto &tile: shape.tiles) {
            size_t tile_hash = std::hash<Tile>{}(tile);
            boost::hash_combine(combined_hash, tile_hash);
        }
        return combined_hash;
    }
};


#endif //TESTING_VOLUME_HPP
