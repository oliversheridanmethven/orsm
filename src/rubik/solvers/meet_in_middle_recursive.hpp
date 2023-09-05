#ifndef TESTING_MEET_IN_MIDDLE_RECURSIVE_HPP
#define TESTING_MEET_IN_MIDDLE_RECURSIVE_HPP

#include "rubik/solvers/solver.hpp"

template<typename S>
class MeetInMiddleRecursive final : Solver<S> {
public:
    virtual Path solve(const S &start, const S &target) const override final {
        Path path;
        return path;
    }
};

#endif //TESTING_MEET_IN_MIDDLE_RECURSIVE_HPP
