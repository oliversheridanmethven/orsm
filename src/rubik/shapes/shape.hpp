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
#include <chrono>

#include "rubik/colours/colour_palette.hpp"
#include "rubik/paths/move.hpp"
#include "rubik/paths/path.hpp"

#include <random>
#include "logging/logging.hpp"
#include <boost/functional/hash.hpp>


class Tile {
public:
    ColourPalette::Colour colour;

    Tile(const ColourPalette::Colour &colour) : colour(colour) {}

    bool operator==(const Tile &other) const {
        return colour == other.colour;
    }

    friend std::hash<Tile>;

    friend std::ostream &operator<<(std::ostream &os, const Tile &tile) {
        os << ColourPalette::name(tile.colour);
        return os;
    }

};

template<>
struct std::hash<Tile> {

    std::size_t operator()(const Tile &tile) const noexcept {
        return std::hash<ColourPalette::enum_underlying>{}(ColourPalette::value(tile.colour));
    }
};


template<typename Self>
class Shape {
public:
    using Tiles = std::vector<Tile>;
    using Row = std::vector<Tile>;
    using Face = std::vector<Row>;
    using Faces = std::vector<Face>;
    using Seed = std::optional<int>;
protected:
    Tiles tiles;

    virtual Faces faces(void) const = 0;

public:

    bool operator==(const Shape &other) const {
        return tiles == other.tiles;
    }

    virtual const std::vector<Move> moves(void) const = 0;

    virtual const std::unordered_map<Move, Move> reverse_moves(void) const = 0;

    virtual const std::vector<std::unordered_set<Move>> commutative_moves(void) const = 0;

    /* In C++ 23, when there is a bit better compiler support, we will use the "deducing this" feature to make derived
     * actions nicer and a cleaner interface for the CRTP pattern. */

    Self move(const std::vector<Move> &moves, const bool reverse = false) const {
        Self moved = *dynamic_cast<const Self *>(this);
        for (const auto &_move: moves) {
            moved = moved.move(_move, reverse);
        }
        return moved;
    }

    Self move(const Move &move, const bool reverse = false) const {
        Self moved;
        auto indices = reverse ? reverse_moves().at(move).indices : move.indices;
        for (size_t i = 0; i < indices.size(); i++) {
            moved.tiles.at(i) = tiles.at(indices.at(i));
        }
        return moved;
    }

    std::pair<Self, Path> shuffle(unsigned int turns, const Seed &seed) const {
        Path path;
        Self shuffled;

        std::random_device rd;
        std::mt19937 gen(rd());
        gen.seed(
                seed.has_value() ? seed.value() : std::chrono::high_resolution_clock::now().time_since_epoch().count());
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

            LOG_TRACE << "turn = " << turn << " shuffling with move: " << move;
            shuffled = shuffled.move(move);
            LOG_DEBUG << "The shuffled shape is: " << shuffled;
            path = path.add(move);
            LOG_DEBUG << "The current path is: " << path;
        }
        return {shuffled, path};

    }

    bool commutative(const Move &move_1, const Move &move_2) const {
        bool any_commutative_groups = false;
        for (auto &commuting_moves: commutative_moves()) {
            if (commuting_moves.contains(move_1)) {
                if (commuting_moves.contains(move_2)) {
                    any_commutative_groups = true;
                }
            }
        }
        return any_commutative_groups;
    }

    Move reverse_of(const Move &move) const {
        return reverse_moves().at(move);
    }

    Self solved_config(void) const {
        Self solved;
        return solved;
    }

    Path clean(const Path &path) const {
        /* Restructures a path in turns of its reciprocal moves performed in the forward direction. */
        Path cleaned = path;
        for (auto &[move, reverse]: cleaned) {
            if (reverse) {
                reverse = false;
                move = this->reverse_of(move);
            }
        }
        return cleaned;
    }

    friend std::hash<Self>;
};

template<typename Self> requires std::is_base_of_v<Shape<Self>, Self>
struct std::hash<Self> {

    std::size_t operator()(const Self &shape) const noexcept {
        size_t combined_hash = 0; /* <- Must be seeded. */
        for (const auto &tile: shape.tiles) {
            size_t tile_hash = std::hash<Tile>{}(tile);
            boost::hash_combine(combined_hash, tile_hash);
        }
        return combined_hash;
    }
};

template<typename T>
std::ostream &operator<<(std::ostream &os, std::vector<T> values) {
    os << "[";
    for (int leading_comma = 0; const auto &value: values) {
        os << (leading_comma++ ? ", " : "") << value;
    }
    os << "]";
    return os;
}


#endif //TESTING_SHAPE_HPP
