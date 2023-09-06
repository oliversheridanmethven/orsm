#include <optional>
#include <iostream>
#include "logging/logging.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/solvers/meet_in_middle_recursive.hpp"
#include "rubik/paths/paths.hpp"
#include "boost/program_options.hpp"

int main(int argc, char **argv) {
    int seed;
    unsigned int turns;

    namespace po = boost::program_options;
    po::options_description desc("Allowed options");
    po::arg = "";
    desc.add_options()
            ("help", "Produce this help message.")
            ("turns", po::value<decltype(turns)>(&turns)->default_value(10)/*->value_name("TURNS")*/,
             "The number of turns.")
            ("verbose", po::bool_switch()->default_value(false), "Set verbose logging level.")
            ("seed", po::value(&seed), "The seed.");


    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    if (vm.count("verbose")) {
        FLAGS_v = 0;
        FLAGS_logtostdout = true;
    }
    google::InitGoogleLogging(argv[0]);

    if (vm.count("help")) {
        std::cout << "Demonstration of the rubik functionality." << "\n\n"
                  << desc << "\n";
        exit(EXIT_SUCCESS);
    }


    Volume shape;
    LOG_INFO << "The initial shape is: " << shape;
    Path solution_path;
    auto [shuffled, shuffle_path] = shape.shuffle(turns, seed);
    LOG_INFO << "The shuffled shape is: " << shuffled
             << "The shuffled shape is constructed by: " << shuffle_path;
    auto solver = MeetInMiddleRecursive<decltype(shape)>();
    solution_path = solver.solve(shape, shuffled);
    LOG_INFO << "The shuffled shape is recovered by: " << solution_path;
}
