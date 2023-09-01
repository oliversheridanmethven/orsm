#include "logging/logging.hpp"
#include "testing/testing.hpp"

Test(logging, minimal_strings)
{
    LOG_INFO << "some info";
    LOG_DEBUG <<"some debug";
    LOG_WARNING <<"some warning";
}

Test(logging, variable_args)
{
    LOG_INFO << "some info" << "some string" << 10;
}

Test(logging, error_fails)
{
    LOG_ERROR << "some error";// This terminates the program.
}
