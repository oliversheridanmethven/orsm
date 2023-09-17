#ifndef TESTING_SHAPE_HPP
#define TESTING_SHAPE_HPP

#include <algorithm>
#include <chrono>
#include <map>
#include <memory>
#include <optional>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "rubiks/moves/move.hpp"
#include "rubiks/paths/path.hpp"
#include "rubiks/shapes/tile.hpp"

#include "logging/logging.hpp"
#include <boost/functional/hash.hpp>

namespace rubiks
{
    namespace shapes
    {
        using namespace rubiks::moves;
        using namespace rubiks::paths;
        using namespace tiles;

        template<typename Self, int N>
        class Shape
        {
        public:
            static const int N_FACES = 6;
            using Tiles = std::array<Tile, N * N * N_FACES>;
            using Row = std::array<Tile, N>;
            using Face = std::array<Row, N>;
            using Faces = std::array<Face, N_FACES>;

        protected:
            Tiles tiles;

            static Faces solved_faces(void)
            {
                Faces faces;
                for (size_t f = 0; const auto &colour: colours::ColourPalette::colours)
                {
                    Face face;
                    for (size_t r = 0, i = 0; i < N; i++)
                    {
                        Row row;
                        for (size_t c = 0, j = 0; j < N; j++)
                        {
                            row.at(c++) = colour;
                        }
                        face.at(r++) = row;
                    }
                    faces.at(f++) = face;
                }
                return faces;
            }

            static Faces faces_of(const Self &shape)
            {
                /* ^ Useful for testing to have a static version. */
                return shape.faces();
            }

            Faces faces(void) const
            {
                auto faces = solved_faces();
                auto _tile = tiles.begin();
                for (auto &face: faces)
                {
                    for (auto &row: face)
                    {
                        for (auto &tile: row)
                        {
                            tile = *(_tile++);
                        }
                    }
                }
                return faces;
            }

        public:
            virtual ~Shape() {}

            bool operator==(const Shape &other) const
            {
                return tiles == other.tiles;
            }

            virtual const std::vector<std::array<size_t, 3>> invariant_tile_positions(void) const = 0;

            virtual const std::vector<Move> moves(void) const = 0;

            virtual const std::unordered_map<Move, Move> reverse_moves(void) const = 0;

            virtual const std::vector<std::unordered_set<Move>> commutative_moves(void) const = 0;

            /* In C++ 23, when there is a bit better compiler support, we will use the "deducing this" feature to make derived
             * actions nicer and a cleaner interface for the CRTP pattern. */

            Self move(const std::vector<Move> &moves, const bool reverse = false) const
            {
                Self moved = static_cast<const Self &>(*this);
                for (const auto &_move: moves)
                {
                    moved = moved.move(_move, reverse);
                }
                return moved;
            }

            Self move(const Move &move, const bool reverse = false) const
            {
                Self moved;
                auto indices = reverse ? reverse_moves().at(move).indices : move.indices;
                for (size_t i = 0; i < indices.size(); i++)
                {
                    moved.tiles.at(i) = tiles.at(indices.at(i));
                }
                return moved;
            }

            bool commutative(const Move &move_1, const Move &move_2) const
            {
                bool any_commutative_groups = false;
                for (auto &commuting_moves: commutative_moves())
                {
                    if (commuting_moves.contains(move_1))
                    {
                        if (commuting_moves.contains(move_2))
                        {
                            any_commutative_groups = true;
                        }
                    }
                }
                return any_commutative_groups;
            }

            Move reverse_of(const Move &move) const
            {
                return reverse_moves().at(move);
            }

            Self solved_config(void) const
            {
                Self solved;
                return solved;
            }

            Path clean(const Path &path) const
            {
                /* Restructures a path in turns of its reciprocal moves performed in the forward direction. */
                Path cleaned = path;
                for (auto &[move, reverse]: cleaned)
                {
                    if (reverse)
                    {
                        reverse = false;
                        move = this->reverse_of(move);
                    }
                }
                return cleaned;
            }

            friend std::hash<Self>;
        };

    }// namespace shapes
}// namespace rubiks

template<typename Self>
    requires std::is_base_of_v<rubiks::shapes::Shape<Self, 2>, Self> or
             std::is_base_of_v<rubiks::shapes::Shape<Self, 3>, Self>
struct std::hash<Self> {
    std::size_t operator()(const Self &shape) const noexcept
    {
        size_t combined_hash = 0; /* <- Must be seeded. */
        for (const auto &tile: shape.tiles)
        {
            size_t tile_hash = std::hash<rubiks::tiles::Tile>{}(tile);
            boost::hash_combine(combined_hash, tile_hash);
        }
        return combined_hash;
    }
};

template<typename T>
std::ostream &operator<<(std::ostream &os, std::vector<T> values)
{
    os << "[";
    for (int leading_comma = 0; const auto &value: values)
    {
        os << (leading_comma++ ? ", " : "") << value;
    }
    os << "]";
    return os;
}

#endif//TESTING_SHAPE_HPP
