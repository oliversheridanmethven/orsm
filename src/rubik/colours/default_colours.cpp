#include "default_colours.hpp"
#include "logging/logging.hpp"
#include <sstream>

std::string ColourPalette::colour(const std::string &s, const Colour &colour) const {
    /*
     * Following the approach outlined here: https://stackoverflow.com/a/45300654/5134817
     *
     * */
    std::stringstream coloured;
    /*
     * The coloured string will have the following ANSI colour code specification:
     * "\033[{FORMAT_ATTRIBUTE};{FORGROUND_COLOR};{BACKGROUND_COLOR}m{TEXT}\033[{RESET_FORMATE_ATTRIBUTE}m"
     *
     * */
    coloured << "\033[0;";
    switch (colour) {
        case Colour::red:
            coloured << "31";
            break;
        case Colour::yellow:
            coloured << "33";
            break;
        case Colour::blue:
            coloured << "34";
            break;
        case Colour::green:
            coloured << "32";
            break;
        case Colour::white:
            coloured << "97";
            break;
        case Colour::light_yellow:
            coloured << "93";
            break;
    }
    coloured << "m" << s << "\033[0m";
    return coloured.str();
}

std::string ColourPalette::name(const Colour &colour) const {
    switch (colour) {
        case Colour::red:
            return "red";
        case Colour::yellow:
            return "orange";
        case Colour::blue:
            return "blue";
        case Colour::green:
            return "green";
        case Colour::white:
            return "white";
        case Colour::light_yellow:
            return "yellow";
    }
    throw std::runtime_error("Unknown colour name encountered.");
}
