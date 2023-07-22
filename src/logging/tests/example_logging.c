/* An example showing how to use logging.
 * When running the executable, use: G_MESSAGES_DEBUG=all ./example_logging
 * To set this with a command line argument, cf. https://stackoverflow.com/a/70019528/5134817
 * */

#include <glib.h> // The logging library of choice.

int main (int argc, char ** argv) {
    g_info("some info");
    g_message("some message");
    g_print("some print\n");
    g_printerr("some print error\n");
    g_debug("some debug");
    g_warning("some warning");
    g_error("some error");  // This terminates the program.
}