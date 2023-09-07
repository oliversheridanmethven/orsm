#ifndef TESTING_CLI_HPP
#define TESTING_CLI_HPP

#include "boost/program_options.hpp"
#include "boost/filesystem.hpp"
#include <string>
#include "version/version.h"
#include <cassert>

namespace cli {
    namespace po = boost::program_options;

    std::vector<std::string> get_unlimited_positional_args_(const po::positional_options_description &p) {
        assert(p.max_total_count() == std::numeric_limits<unsigned>::max());

        std::vector<std::string> parts;

        // reasonable upper limit for number of positional options:
        const int MAX = 1000;
        std::string last = p.name_for_position(MAX);

        for (size_t i = 0; true; ++i) {
            std::string cur = p.name_for_position(i);
            if (cur == last) {
                parts.push_back(cur);
                parts.push_back('[' + cur + ']');
                parts.push_back("...");
                return parts;
            }
            parts.push_back(cur);
        }
        return parts; // never get here
    }

    std::string make_usage_string_(const std::string &program_name, const po::options_description &desc,
                                   po::positional_options_description &p) {
        /* Taken from https://gist.github.com/ksimek/4a2814ba7d74f778bbee */

        std::vector<std::string> parts;
        parts.push_back("Usage:\n\t");
        parts.push_back(program_name);
        size_t N = p.max_total_count();
        if (N == std::numeric_limits<unsigned>::max()) {
            std::vector<std::string> args = get_unlimited_positional_args_(p);
            parts.insert(parts.end(), args.begin(), args.end());
        } else {
            for (size_t i = 0; i < N; ++i) {
                parts.push_back(p.name_for_position(i));
            }
        }
        if (desc.options().size() > 0) {
            parts.push_back("[options]");
        }
        std::ostringstream oss;
        std::copy(
                parts.begin(),
                parts.end(),
                std::ostream_iterator<std::string>(oss, " "));
        oss << "\n\n" << desc;
        return oss.str();
    }


    auto setup_standard_parser(int argc, char **argv, std::string description = "") {
        std::stringstream _epilogue;
        _epilogue << "\nVersion:\n\t" << repo_name() << " " << repo_version() << "\n";
        _epilogue << "\nAuthor:\n\t" << repo_author() << "\n";
        _epilogue << "\nMaintained by:\n\t" << repo_author() << " " << repo_email() << "\n";
        std::string epilogue = _epilogue.str();

        po::options_description options("Allowed options");
        po::positional_options_description positional_options;
        
        po::arg = "";
        options.add_options()
                ("help", "Show this help message.")
                ("version", "Show the version of this program.")
                ("verbose", po::bool_switch()->default_value(false), "Set verbose logging level.")
                ("debug", po::bool_switch()->default_value(false), "Set debug logging level.")
                ("trace", po::bool_switch()->default_value(false), "Set trace logging level.");

        auto finalise = [=](po::options_description options, po::positional_options_description positional_options) {
            po::variables_map vm;
            po::store(po::parse_command_line(argc, argv, options), vm);
            po::notify(vm);

            if (vm["verbose"].as<bool>()) {
                FLAGS_v = INFO_LEVEL;
                FLAGS_logtostdout = true;
            }

            if (vm["debug"].as<bool>()) {
                FLAGS_v = DEBUG_LEVEL;
                FLAGS_logtostdout = true;
            }

            if (vm["trace"].as<bool>()) {
                FLAGS_v = TRACE_LEVEL;
                FLAGS_logtostdout = true;
            }

            google::InitGoogleLogging(argv[0]);

            if (vm.count("help")) {
                std::cout << "\n"
                          << description << "\n\n"
                          << make_usage_string_(boost::filesystem::path(argv[0]).stem().string(), options,
                                                positional_options)
                          //                          << options << "\n"
                          << epilogue << "\n";
                exit(EXIT_SUCCESS);
            }

            if (vm.count("version")) {
                std::cout << repo_version() << "\n";
                exit(EXIT_SUCCESS);
            }
        };

        return std::make_tuple(options, positional_options, finalise);

    }
}
#endif //TESTING_CLI_HPP
