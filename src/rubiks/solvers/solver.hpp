#ifndef TESTING_SOLVER_HPP
#define TESTING_SOLVER_HPP

#include "rubiks/paths/path.hpp"
#include "rubiks/shapes/shape.hpp"

namespace rubiks
{
    namespace solvers
    {
        using namespace rubiks::paths;

        template<typename Shape>
        class Solver
        {
        public:
            virtual Path solve(const Shape &start, const Shape &target) const = 0;
        };
    }// namespace solvers
}// namespace rubiks

#endif//TESTING_SOLVER_HPP
