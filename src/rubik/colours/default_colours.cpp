#include "default_colours.hpp"

#include <sstream>

std::string Colour::colour(const std::string &s) const {
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
        case _Colours::red:
            coloured << "31";
            break;
        case _Colours::yellow:
            coloured << "33";
            break;
        case _Colours::blue:
            coloured << "34";
            break;
        case _Colours::green:
            coloured << "32";
            break;
        case _Colours::white:
            coloured << "97";
            break;
        case _Colours::light_yellow:
            coloured << "93";
            break;
    }
    coloured << s << "\033[0m";
    return coloured.str();
}
