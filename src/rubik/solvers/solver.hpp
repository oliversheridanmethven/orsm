#ifndef TESTING_SOLVER_HPP
#define TESTING_SOLVER_HPP

#include "rubik/shapes/shape.hpp"
#include "rubik/paths/paths.hpp"

template<typename S>
class Solver {
public:
    virtual Path solve(const S &start, const S &target) const = 0;
};

#endif //TESTING_SOLVER_HPP
