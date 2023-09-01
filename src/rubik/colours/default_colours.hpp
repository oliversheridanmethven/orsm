#ifndef TESTING_DEFAULT_COLOURS_HPP
#define TESTING_DEFAULT_COLOURS_HPP

#include <string>

class Colour {
private:
    enum class _Colours {
        red = 0,
        yellow,
        blue,
        green,
        white,
        light_yellow
    };

    _Colours _colour;

public:
    std::string colour(const std::string &s) const;
};

#endif //TESTING_DEFAULT_COLOURS_HPP
