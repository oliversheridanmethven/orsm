#ifndef TESTING_DEFAULT_COLOURS_HPP
#define TESTING_DEFAULT_COLOURS_HPP

#include <string>
#include <vector>


class ColourPalette {
public:
    using enum_underlying = int;

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

    static std::string name(const Colour &colour);

    static std::string colour(const std::string &s, const Colour &colour);

    static enum_underlying value(const Colour &colour);
};

#endif //TESTING_DEFAULT_COLOURS_HPP
