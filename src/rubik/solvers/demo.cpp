#include <optional>
#include <iostream>
#include "logging/logging.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/solvers/meet_in_middle_recursive.hpp"
#include "rubik/paths/paths.hpp"
#include "common/cli.hpp"
#include <ranges>

int main(int argc, char **argv) {
    int seed;
    unsigned int turns;

    auto [options, positional_options, parser_finalise] = cli::setup_standard_parser(argc, argv,
                                                                                     "Demonstration of solving Rubik style puzzles.");

    options.add_options()
            ("turns",
             cli::po::value<decltype(turns)>(&turns)->default_value(100)/*->value_name("TURNS")*/,
             "The number of turns.")
            ("seed", cli::po::value(&seed), "The seed.");

    parser_finalise(options, positional_options);


    Volume shape;
    LOG_INFO << "The initial shape is: " << shape;
    Path solution_path;
    auto [shuffled, shuffle_path] = shape.shuffle(turns, seed);
    LOG_INFO << "The shuffled shape is: " << shuffled;
    LOG_INFO << "The shuffled shape is constructed by:\n" << shuffle_path << "\n";
    auto solver = MeetInMiddleRecursive<decltype(shape)>();
    solution_path = solver.solve(shape, shuffled);
    LOG_INFO << "The shuffled shape is recovered by: " << solution_path;
}
