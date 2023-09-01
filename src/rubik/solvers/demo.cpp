#include <optional>
#include <iostream>
#include "logging/logging.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/solvers/meet_in_middle_recursive.hpp"
#include "rubik/paths/paths.hpp"
#include "rubik/paths/paths.hpp"

int main(int argc, char **argv) {
    LOG_INIT(argv);

    std::optional<int> seed;
    int turns;
    Volume shape, shuffled;
    Path shuffle_path, solution_path;
    shuffled, shuffle_path = shape.shuffle(turns, seed);
    solution_path = meet_in_middle_recursive();
    std::cout << "The initial shape was: " << shape
              << "The shuffled shape is: " << shuffled
              << "The shuffled shape is constructed by: " << shuffle_path
              << "The shuffled shape is recovered by: " << solution_path;
}
