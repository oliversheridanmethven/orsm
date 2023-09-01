#include "paths.hpp"

void Path::append(const Move &move, const bool) {}

Path Path::add(const Move &move, const bool reverse) {
    Path result = *this;
    result.append(move, reverse);
    return result;
}
