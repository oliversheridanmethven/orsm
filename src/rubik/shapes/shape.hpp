#ifndef TESTING_SHAPE_HPP
#define TESTING_SHAPE_HPP

#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <memory>
#include <optional>
#include <algorithm>

#include "rubik/colours/default_colours.hpp"
#include "rubik/paths/moves.hpp"
#include "rubik/paths/paths.hpp"

#include <random>
#include "logging/logging.hpp"

class Tile {
public:
    ColourPalette::Colour colour;

    Tile(const ColourPalette::Colour &colour) : colour(colour) {}
};

template<typename Self>
class Shape {
protected:
    std::vector<Tile> tiles;
    using Row = std::vector<Tile>;
    using Face = std::vector<Row>;
    using Faces = std::vector<Face>;

    virtual Faces faces(void) const = 0;


public:
    virtual const std::vector<Move> moves(void) const = 0;

    virtual const std::unordered_map<Move, Move> reverse_moves(void) const = 0;

    virtual const std::vector<std::unordered_set<Move>> commutative_moves(void) const = 0;

    /* In C++ 23, when there is a bit better compiler support, we will use the "deducing this" feature to make derived
     * actions nicer and a cleaner interface for the CRTP pattern. */

    Self move(const Move &move, const bool reverse = false) const {
        Self moved;
        auto indices = reverse ? reverse_moves().at(move).indices : move.indices;
        for (size_t i = 0; i < indices.size(); i++) {
            moved.tiles.at(i) = tiles.at(indices.at(i));
        }
        return moved;
    }

    std::pair<Self, Path> shuffle(unsigned int turns, std::optional<int> seed) const {
        Path path;
        Self shuffled;

        std::random_device rd;
        std::mt19937 gen(rd());
        std::optional<Move> last_move;
        for (decltype(turns) turn = 0; turn < turns; turn++) {
            Move move;
            while (true) {
                auto possible_moves = moves();
                std::sample(possible_moves.begin(), possible_moves.end(), &move, 1, gen);
                if (last_move and commutative(move, last_move.value())) {
                    continue;
                }
                last_move = move;
                break;
            }

            LOG_INFO << "turn = " << turn << " shuffling with move: " << move;
            shuffled = shuffled.move(move);
            LOG_DEBUG << "The shuffled shape is: " << shuffled;
            path = path.add(move);
        }
        return {shuffled, path};

    }

    bool commutative(const Move &move_1, const Move &move_2) const {
        for (auto &commuting_moves: commutative_moves()) {
            if (commuting_moves.contains(move_1)) {
                return commuting_moves.contains(move_2);
            }
        }
        throw std::runtime_error("We could not find a commutative grouping containing our moves.");
    }

};


#endif //TESTING_SHAPE_HPP
