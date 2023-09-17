#ifndef TESTING_TILE_HPP
#define TESTING_TILE_HPP

#include "rubiks/colours/colour_palette.hpp"

namespace rubiks
{
    namespace tiles
    {

        using namespace colours;

        // TODO: Make this a literal type so I can use in in consteval expressions.
        class Tile
        {
        public:
            ColourPalette::Colour colour;

            Tile() {}

            Tile(const ColourPalette::Colour &colour) : colour(colour) {}

            bool operator==(const Tile &other) const
            {
                return colour == other.colour;
            }

            friend std::ostream &operator<<(std::ostream &os, const Tile &tile)
            {
                os << ColourPalette::name(tile.colour);
                return os;
            }
        };

    }// namespace tiles
}// namespace rubiks

template<>
struct std::hash<rubiks::tiles::Tile> {
    std::size_t operator()(const rubiks::tiles::Tile &tile) const noexcept
    {
        return std::hash<colours::ColourPalette::enum_underlying>{}(colours::ColourPalette::value(tile.colour));
    }
};

#endif//TESTING_TILE_HPP
