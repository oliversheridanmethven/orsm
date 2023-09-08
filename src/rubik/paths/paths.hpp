#ifndef TESTING_PATHS_HPP
#define TESTING_PATHS_HPP

#include "moves.hpp"
#include <vector>

class Path {
private:

    void append(const Move &move, const bool);

public:
    std::vector<Move> moves;
    std::vector<bool> reverses;

    Path add(const Move &move, const bool reverse = false);

    bool operator==(const Path &other) const {
        return moves == other.moves and reverses == other.reverses;
    }

    friend std::ostream &operator<<(std::ostream &os, const Path &path) {
        if (path.moves.empty()) {
            os << "Empty path.\n";
            return os;
        }
        for (size_t turn = 0; turn < path.moves.size(); turn++) {
            os << "\nTurn = " << turn << " " << path.moves[turn] << (path.reverses[turn] ? " in reverse" : "");
        }
        os << "\n";
        return os;
    }

    auto begin() const {}
};

#endif //TESTING_PATHS_HPP
