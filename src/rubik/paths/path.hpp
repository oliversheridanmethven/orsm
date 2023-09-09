#ifndef TESTING_PATH_HPP
#define TESTING_PATH_HPP

#include "move.hpp"
#include <vector>

using Reverse = bool;

class Path : public std::vector<std::tuple<Move, Reverse>> {

public:

    Path add(const Move &move, const bool reverse = false) const;

    Path reversed(void) const;

    friend std::ostream &operator<<(std::ostream &os, const Path &path) {
        if (path.empty()) {
            os << "Empty path.\n";
            return os;
        }

        for (size_t turn = 0; auto [move, reverse]: path) {
            os << "\nTurn = " << turn++ << " " << move << (reverse ? " in reverse" : "");
        }
        os << "\n";
        return os;
    }
};

#endif //TESTING_PATH_HPP
