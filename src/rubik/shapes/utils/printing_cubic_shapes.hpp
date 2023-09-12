#ifndef TESTING_PRINTING_CUBIC_SHAPES_HPP
#define TESTING_PRINTING_CUBIC_SHAPES_HPP

#include <string>
#include <sstream>

namespace cubic_shapes {

    auto to_string(const auto &faces, const auto &colour_palette) {
        auto front = faces[0];
        auto back = faces[1];
        auto right = faces[2];
        auto left = faces[3];
        auto top = faces[4];
        auto bottom = faces[5];
        std::stringstream s, bars;
        s << "\n\n";
        size_t indent = 1 + 2 * top.size();
        auto indenting = indent + 1 + top.size();
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
        return s.str();
    }

}

#endif //TESTING_PRINTING_CUBIC_SHAPES_HPP
