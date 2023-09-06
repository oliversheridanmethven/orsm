#include "paths.hpp"

void Path::append(const Move &move, const bool reverse) {
    moves.push_back(move);
    reverses.push_back(reverse);
}

Path Path::add(const Move &move, const bool reverse) {
    Path result = *this;
    result.append(move, reverse);
    return result;
}
