#ifndef TESTING_SOLVER_HPP
#define TESTING_SOLVER_HPP

#include "rubik/shapes/shape.hpp"
#include "rubik/paths/path.hpp"

template<typename Shape>
class Solver {
public:
    virtual Path solve(const Shape &start, const Shape &target) const = 0;
};

#endif //TESTING_SOLVER_HPP
