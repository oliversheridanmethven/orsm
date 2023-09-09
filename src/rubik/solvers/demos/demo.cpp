#include <optional>
#include <iostream>
#include "logging/logging.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/solvers/meet_in_middle_recursive.hpp"
#include "rubik/paths/path.hpp"
#include "common/cli.hpp"
#include <ranges>
#include <boost/optional.hpp>

int main(int argc, char **argv) {

    /* Boost doesn't play perfectly well with std::optional yet. cf.:
     * https://stackoverflow.com/a/66548554/5134817
     * https://stackoverflow.com/q/76928378/5134817
     * */
    using Seed = boost::optional<typename Volume::Seed::value_type>;

    Seed _seed;
    unsigned int turns;

    auto [options, positional_options, parser_finalise] = cli::standard_parser_setup(argc, argv,
                                                                                     "Demonstration of solving Rubik style puzzles.");

    options.add_options()
            ("turns",
             cli::po::value(&turns)->default_value(100)/*->value_name("TURNS")*/,
             "The number of turns.")
            ("seed", cli::po::value(&_seed)->default_value(Seed{}, "None"), "The seed.");

    parser_finalise(options, positional_options);
    typename Volume::Seed seed;
    if (_seed.has_value()) {
        seed = _seed.value();
    }

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
