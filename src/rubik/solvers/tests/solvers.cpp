#include "testing/testing.h"
#include "rubik/shapes/shape.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/shapes/cube.hpp"
#include "rubik/shufflers/shufflers.hpp"
#include "rubik/solvers/meet_in_middle_recursive.hpp"


template<typename S>
class ShapeSolverTest : public testing::Test {
};

using ShapeTypes = ::testing::Types<Volume, Cube>;
TYPED_TEST_SUITE(ShapeSolverTest, ShapeTypes);

auto check_solution_recovers_shuffled(const auto &original, const auto &shuffled, const auto &solution_path,
                                      const auto &shuffle_path) {
    auto solution = original;
    for (const auto &[move, reverse]: solution_path) {
        solution = solution.move(move, reverse);
    }
    LOG_DEBUG << "We are comparing the solution " << solution << " with the shuffled " << shuffled;
    ASSERT_EQ(solution, shuffled) << "We do not arrive at the target using the solution moves.";
    solution = shuffled;
    for (const auto &[move, reverse]: solution_path.reversed()) {
        solution = solution.move(move, reverse);
    }
    ASSERT_EQ(solution, original) << "We do not arrive at the start using the solution moves in reverse.";
}


TYPED_TEST(ShapeSolverTest, solver) {
    std::vector solvers = {MeetInMiddleRecursive<TypeParam>()};
    for (const auto &solver: solvers) {
        TypeParam shape;
        for (size_t turns = 0, seed = 0; turns < 6; turns++) {
            auto [shuffled, shuffle_path] = shape.shuffle(turns, seed);
            auto solution_path = solver.solve(shape, shuffled);
            ASSERT_LE(solution_path.size(), shuffle_path.size())
                                        << "The solution path for {solver_name} is not optimal, as it takes more moves than we used to shuffle our shape.";
            LOG_DEBUG << "The original shape is: " << shape
                      << "The shuffled shape is: " << shuffled
                      << "The shuffled shape was achieved by: " << shuffle_path
                      << "The original shape is recovered (hopefully) by: " << solution_path;
            check_solution_recovers_shuffled(shape, shuffled, solution_path, shuffle_path);
        }
    }
}

TYPED_TEST(ShapeSolverTest, specific_difficulty) {
    std::vector solvers = {MeetInMiddleRecursive<TypeParam>()};
    for (const auto &solver: solvers) {
        TypeParam shape;
        for (int turns = 0; turns < 5; turns++) {
            std::variant<int, std::string> _turns = turns;
            std::optional<int> seed = 0;
            auto [shuffled, shuffle_path] = specific(shape, _turns, seed);
            ASSERT_EQ(shuffle_path.size(), turns)
                                        << "We have not generated a shuffled path with the required number of turns.";
            auto solution_path = solver.solve(shape, shuffled);
            ASSERT_LE(solution_path.size(), shuffle_path.size())
                                        << "The solution path is not optimal, as it takes more moves than we used to shuffle our shape.";
            ASSERT_EQ(solution_path.size(), turns) << "Our solution path is not the right length.";
            check_solution_recovers_shuffled(shape, shuffled, solution_path,
                                             shuffle_path);
        }
    }
}

