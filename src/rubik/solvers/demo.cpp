#include <optional>
#include <iostream>
#include "logging/logging.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/solvers/meet_in_middle_recursive.hpp"
#include "rubik/paths/paths.hpp"
#include "rubik/paths/paths.hpp"
#include "boost/program_options.hpp"

int main(int argc, char **argv) {
    LOG_INIT(argv);
    int seed;
    unsigned int turns;

    namespace po = boost::program_options;
    po::options_description desc("Demonstrate the rubik functionality.");
    desc.add_options()
            ("help", "Produce this help message.")
            ("turns", po::value<decltype(turns)>(&turns)->default_value(10), "The number of turns.")
            ("seed", po::value(&seed), "The seed.");


    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    if (vm.count("help")) {
        std::cout << desc << "\n";
        exit(EXIT_SUCCESS);
    }


    Volume shape;
    Path solution_path;
    auto [shuffled, shuffle_path] = shape.shuffle(turns, seed);
    auto solver = MeetInMiddleRecursive<decltype(shape)>();
    solution_path = solver.solve(shape, shuffled);
    std::cout << "The initial shape was: " << shape
              << "The shuffled shape is: " << shuffled
              << "The shuffled shape is constructed by: " << shuffle_path
              << "The shuffled shape is recovered by: " << solution_path;
}
