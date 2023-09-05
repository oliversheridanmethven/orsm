#ifndef TESTING_PATHS_HPP
#define TESTING_PATHS_HPP

#include "moves.hpp"
#include <vector>

class Path {
private:
    std::vector<Move> _moves;
    std::vector<bool> _reverses;

    void append(const Move &move, const bool);

public:
    Path add(const Move &move, const bool reverse = false);

    friend std::ostream &operator<<(std::ostream &os, const Path &path) {
        if (path._moves.empty()) {
            os << "Empty path.\n";
            return os;
        }
        for (size_t turn = 0; turn < path._moves.size(); turn++) {
            os << "\nTurn = " << turn << " " << path._moves[turn] << (path._reverses[turn] ? " in reverse" : "");
        }
        os << "\n";
        return os;
    }
};

#endif //TESTING_PATHS_HPP
