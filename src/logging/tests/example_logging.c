/* An example showing how to use logging.
 * When running the executable, use: G_MESSAGES_DEBUG=all ./example_logging
 * To set this with a command line argument, cf. https://stackoverflow.com/a/70019528/5134817
 * */

#include "logging/logging.h"

int main (int argc, char ** argv) {
    INFO("some info");
    MESSAGE("some message");
    PRINT("some print\n");
    PRINTERR("some print error\n");
    DEBUG("some debug");
    WARNING("some warning");
    g_error("some error");  // This terminates the program.
}