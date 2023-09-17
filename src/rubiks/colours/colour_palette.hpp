#ifndef TESTING_COLOUR_PALETTE_HPP
#define TESTING_COLOUR_PALETTE_HPP

#include <string>
#include <vector>

namespace colours
{
    class ColourPalette
    {
    public:
        using enum_underlying = int;

        enum class Colour : enum_underlying
        {
            red = 0,
            yellow,
            blue,
            green,
            white,
            light_yellow
        };

        // Iterating through an enum class is a nightmare, so we have this small helper function.
        static const std::vector<Colour> colours;

        static std::string name(const Colour &colour);

        static std::string colour(const std::string &s, const Colour &colour);

        static enum_underlying value(const Colour &colour);
    };
}// namespace colours

#endif//TESTING_COLOUR_PALETTE_HPP
