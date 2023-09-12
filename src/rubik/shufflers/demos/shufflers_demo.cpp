#include "common/cli.hpp"
#include "boost/optional.hpp"
#include "rubik/shapes/volume.hpp"
#include "rubik/shufflers/shufflers.hpp"

int main(int argc, char **argv) {
    using Seed = boost::optional<typename Volume::Seed::value_type>;

    Seed _seed;
    int turns;

    auto [options, positional_options, parser_finalise] = cli::standard_parser_setup(argc, argv,
                                                                                     "A small demonstration of how to use some shufflers (useful for profiling.)");

    options.add_options()
            ("turns",
             cli::po::value(&turns)->default_value(7)/*->value_name("TURNS")*/,
             "The number of turns.")
            ("seed", cli::po::value(&_seed)->default_value(Seed{}, "None"), "The seed.");

    parser_finalise(options, positional_options);
    typename Volume::Seed seed;
    if (_seed.has_value()) {
        seed = _seed.value();
    }

    Volume shape;
    auto ignore = specific(shape, turns, seed);

}