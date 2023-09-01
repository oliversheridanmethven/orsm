#ifndef TESTING_SHAPE_HPP
#define TESTING_SHAPE_HPP

#include <string>
#include <vector>
#include <memory>
#include <optional>

#include "rubik/paths/moves.hpp"
#include "rubik/paths/paths.hpp"
#include "rubik/colours/default_colours.hpp"

class Tile {
private:
    Colour colour;
};

class Shape {
private:
    std::vector<Tile> _tiles;
    std::vector<std::vector<std::vector<Tile>>> _faces;

public:
    const std::vector<Move> moves;

    template<typename Self>
    Self move(this Self &&self, const Move &move, const bool reverse = false) const = 0;

    template<typename Self>
    std::pair<Self, Path> shuffle(this Self &&self, unsigned int turns, std::optional<int> seed) const;

};


#endif //TESTING_SHAPE_HPP
