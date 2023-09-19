#include "colour_palette.hpp"
#include "logging/logging.hpp"
#include <sstream>

namespace colours
{

    std::string ColourPalette::colour(const std::string &s, const Colour &colour)
    {
        /*
     * Following the approach outlined here: https://stackoverflow.com/a/45300654/5134817
     *
     * */
        std::stringstream coloured;
        /*
     * The coloured string will have the following ANSI colour code specification:
     * "\033[{FORMAT_ATTRIBUTE};{FOREGROUND_COLOR};{BACKGROUND_COLOR}m{TEXT}\033[{RESET_FORMATE_ATTRIBUTE}m"
     *
     * */
        coloured << "\033[0;";
        switch (colour)
        {
            using enum ColourPalette::Colour;
            case red:
                coloured << "31";
                break;
            case yellow:
                coloured << "33";
                break;
            case blue:
                coloured << "34";
                break;
            case green:
                coloured << "32";
                break;
            case white:
                coloured << "97";
                break;
            case light_yellow:
                coloured << "93";
                break;
        }
        coloured << "m" << s << "\033[0m";
        return coloured.str();
    }

    std::string ColourPalette::name(const Colour &colour)
    {
        switch (colour)
        {
            using enum ColourPalette::Colour;

            case red:
                return "red";
            case yellow:
                return "orange";
            case blue:
                return "blue";
            case green:
                return "green";
            case white:
                return "white";
            case light_yellow:
                return "yellow";
        }
        throw std::runtime_error("Unknown colour name encountered.");
    }

    ColourPalette::enum_underlying ColourPalette::value(const Colour &colour)
    {
        return static_cast<std::underlying_type<std::decay<decltype(colour)>::type>::type>(colour);
    }

    using enum ColourPalette::Colour;
    const std::vector<ColourPalette::Colour> ColourPalette::colours = {red,
                                                                       yellow,
                                                                       blue,
                                                                       green,
                                                                       white,
                                                                       light_yellow};
}// namespace colours
