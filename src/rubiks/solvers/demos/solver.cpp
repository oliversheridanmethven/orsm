#include "common/cli.hpp"
#include "logging/logging.hpp"
#include "rubiks/shapes/cube.hpp"
#include "rubiks/shapes/volume.hpp"
#include "rubiks/shufflers/seed.hpp"
#include "rubiks/shufflers/shuffle.hpp"
#include "rubiks/solvers/meet_in_middle_recursive.hpp"
#include <boost/optional.hpp>
#include <iostream>
#include <optional>
#include <variant>

using namespace rubiks::shapes::cubics;
using namespace rubiks::paths;
using namespace rubiks::shufflers;
using namespace rubiks::solvers;

int main(int argc, char **argv)
{

    /* Boost doesn't play perfectly well with std::optional yet. cf.:
     * https://stackoverflow.com/a/66548554/5134817
     * https://stackoverflow.com/q/76928378/5134817
     * */
    using Seed_ = boost::optional<typename Seed::value_type>;

    Seed_ _seed;
    unsigned int turns;
    std::string shape_name;
    auto [options, positional_options, parser_finalise] = cli::standard_parser_setup(argc, argv,
                                                                                     "Demonstration of solving Rubik style puzzles.");

    options.add_options()("turns",
                          cli::po::value(&turns)->default_value(6) /*->value_name("TURNS")*/,
                          "The number of turns.")("seed", cli::po::value(&_seed)->default_value(Seed_{}, "None"), "The seed.")("shape", cli::po::value(&shape_name)->default_value("Cube"), "The shape.");

    parser_finalise(options, positional_options);
    Seed seed;
    if (_seed.has_value())
    {
        seed = _seed.value();
    }

    Volume volume;
    Cube cube;
    std::variant<Volume, Cube> shapes;
    if (shape_name == "Volume")
    {
        shapes = volume;
    }
    else if (shape_name == "Cube")
    {
        shapes = cube;
    }
    else
    {
        LOG_CRITICAL << "Unknown shape name specified: " << shape_name;
    }

    std::visit([=](auto shape) {
        LOG_INFO << "The initial shape is: " << shape;
        Path solution_path;
        auto [shuffled, shuffle_path] = shuffle(shape, turns, seed);
        LOG_INFO << "The shuffled shape is constructed by:\n"
                 << shuffle_path << "\n";
        LOG_INFO << "The shuffled shape is: " << shuffled;
        auto solver = MeetInMiddleRecursive<decltype(shape)>();
        solution_path = solver.solve(shape, shuffled);
        LOG_DEBUG << "The shuffled shape is recovered by: " << solution_path;
        LOG_INFO << "The original shape is recovered by: " << clean(solution_path.reversed(), shape);
    },
               shapes);
}
