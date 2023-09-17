#include "boost/optional.hpp"
#include "common/cli.hpp"
#include "rubiks/shapes/volume.hpp"
#include "rubiks/shufflers/seed.hpp"
#include "rubiks/shufflers/shufflers.hpp"

using namespace rubiks::shapes::cubics;
using namespace rubiks::shufflers;

int main(int argc, char **argv)
{
    using Seed_ = boost::optional<typename Seed::value_type>;

    Seed_ _seed;
    int turns;

    auto [options, positional_options, parser_finalise] = cli::standard_parser_setup(argc, argv,
                                                                                     "A small demonstration of how to use some shufflers (useful for profiling.)");

    options.add_options()("turns",
                          cli::po::value(&turns)->default_value(7) /*->value_name("TURNS")*/,
                          "The number of turns.")("seed", cli::po::value(&_seed)->default_value(Seed_{}, "None"), "The seed.");

    parser_finalise(options, positional_options);
    Seed seed;
    if (_seed.has_value())
    {
        seed = _seed.value();
    }

    Volume shape;
    auto ignore = specific(shape, turns, seed);
}
