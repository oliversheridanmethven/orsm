//#include "common/cli.hpp"

#ifndef TESTING_CLI_HPP
#define TESTING_CLI_HPP

#include "boost/program_options.hpp"
//#include "boost/filesystem.hpp"
#include "version/version.h"
#include <cassert>
#include <iostream>
#include <string>
#include <sstream>
#include <tuple>
//#include "logging/logging.hpp"

namespace cli {
    namespace po = boost::program_options;

    auto standard_parser_setup(int argc, char **argv) {

        po::options_description options;

        bool dummy;
        int foo;

//        po::arg = ""; /* <- gcc doesn't like this. */
        options.add_options()
                ("help", "Show this help message.")
                ("version", "Show the version of this program.")
                ("verbose", po::bool_switch(&dummy), "Set verbose logging level.")
                ("foo", po::value(&foo), "Set verbose logging level.")
//                ("debug", po::bool_switch()->default_value(false), "Set debug logging level.")
//                ("trace", po::bool_switch()->default_value(false), "Set trace logging level.")
                ;

        return options;

    }

    void
    standard_parser_finalise(int argc, char **argv, /*const po::options_description &options,*/
                             std::string description) {
//                std::stringstream _epilogue;
//        _epilogue << "\nVersion:\n\t" << repo_name() << " " << repo_version() << "\n";
//        _epilogue << "\nAuthor:\n\t" << repo_author() << "\n";
//        _epilogue << "\nMaintained by:\n\t" << repo_author() << " " << repo_email() << "\n";
//        std::string epilogue/* = _epilogue.str()*/;
//        po::variables_map vm;
//        po::store(po::parse_command_line(argc, argv, options), vm);
//        po::notify(vm);
//
//        if (vm["verbose"].as<bool>()) {
//            FLAGS_v = INFO_LEVEL;
//            FLAGS_logtostdout = true;
//        }
//
//        if (vm["debug"].as<bool>()) {
//            FLAGS_v = DEBUG_LEVEL;
//            FLAGS_logtostdout = true;
//        }
//
//        if (vm["trace"].as<bool>()) {
//            FLAGS_v = TRACE_LEVEL;
//            FLAGS_logtostdout = true;
//        }
//
//        google::InitGoogleLogging(argv[0]);
//
//        if (vm.count("help")) {
//            std::cout << "\n"
//                      << description << "\n\n"
//                      << "Usage:\n"
//                      << options << "\n"
////                          << epilogue << "\n"
//                    ;
//            exit(EXIT_SUCCESS);
//        }
//
//        if (vm.count("version")) {
//            std::cout << repo_version() << "\n";
//            exit(EXIT_SUCCESS);
//        }
    };
}
#endif //TESTING_CLI_HPP


int main() {

}
