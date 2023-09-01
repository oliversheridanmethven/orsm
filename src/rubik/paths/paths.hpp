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
    Path add(const Move &move, const bool reverse = False);
};

#endif //TESTING_PATHS_HPP
