#ifndef TESTING_PATH_HPP
#define TESTING_PATH_HPP

#include "rubiks/moves/move.hpp"
#include <vector>

namespace rubiks
{
    namespace paths
    {
        using namespace rubiks::moves;
        using Reverse = bool;

        class Path : public std::vector<std::tuple<Move, Reverse>>
        {

        public:
            Path add(const Move &move, const bool reverse = false) const;

            Path reversed(void) const;

            friend std::ostream &operator<<(std::ostream &os, const Path &path);
        };

        auto clean(const Path &path, const auto &shape)
        {
            /* Restructures a path in turns of its reciprocal moves performed in the forward direction. */
            auto cleaned = path;
            for (auto &[move, reverse]: cleaned)
            {
                if (reverse)
                {
                    reverse = false;
                    move = shape.reverse_of(move);
                }
            }
            return cleaned;
        }

    }// namespace paths
}// namespace rubiks

#endif//TESTING_PATH_HPP
