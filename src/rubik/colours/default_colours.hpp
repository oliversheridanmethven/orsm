#ifndef TESTING_DEFAULT_COLOURS_HPP
#define TESTING_DEFAULT_COLOURS_HPP

#include <string>

using enum_underlying = int;

class ColourPalette {
public:

    enum class Colours : enum_underlying {
        red = 0,
        yellow,
        blue,
        green,
        white,
        light_yellow
    };


    std::string name(const Colours &colour) const;

    Colours something = Colours::red;

    std::string colour(const std::string &s) const;

    enum_underlying value(const Colours &colour) const {
        return static_cast<typename std::underlying_type<Colours>::type>(colour);
    }

private:
    Colours _colour;
};

#endif //TESTING_DEFAULT_COLOURS_HPP
