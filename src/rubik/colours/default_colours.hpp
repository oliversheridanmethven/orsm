#ifndef TESTING_DEFAULT_COLOURS_HPP
#define TESTING_DEFAULT_COLOURS_HPP

#include <string>
#include <vector>

using enum_underlying = int;

class ColourPalette {
public:

    enum class Colour : enum_underlying {
        red = 0,
        yellow,
        blue,
        green,
        white,
        light_yellow
    };

    // Iterating through an enum class is a nightmare, so we have this small helper function.
    const std::vector<Colour> colours = {Colour::red,
                                         Colour::yellow,
                                         Colour::blue,
                                         Colour::green,
                                         Colour::white,
                                         Colour::light_yellow};

    std::string name(const Colour &colour) const;

    Colour something = Colour::red;

    std::string colour(const std::string &s, const Colour &colour) const;

    enum_underlying value(const Colour &colour) const {
        return static_cast<typename std::underlying_type<Colour>::type>(colour);
    }
};

#endif //TESTING_DEFAULT_COLOURS_HPP
