#include "default_colours.hpp"
#include "logging/logging.hpp"
#include <sstream>

std::string ColourPalette::colour(const std::string &s) const {
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
    switch (this->_colour) {
        case Colours::red:
            coloured << "31";
            break;
        case Colours::yellow:
            coloured << "33";
            break;
        case Colours::blue:
            coloured << "34";
            break;
        case Colours::green:
            coloured << "32";
            break;
        case Colours::white:
            coloured << "97";
            break;
        case Colours::light_yellow:
            coloured << "93";
            break;
    }
    coloured << s << "\033[0m";
    return coloured.str();
}

std::string ColourPalette::name(const Colours &colour) const {
    switch (colour) {
        case Colours::red:
            return "red";
        case Colours::yellow:
            return "orange";
        case Colours::blue:
            return "blue";
        case Colours::green:
            return "green";
        case Colours::white:
            return "white";
        case Colours::light_yellow:
            return "yellow";
    }
    throw std::runtime_error("Unknown colour name encountered.");
}
