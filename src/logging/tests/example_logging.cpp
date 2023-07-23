#include <glib.h>// The logging library of choice.

int main(int argc, char **argv)
{
    g_info("some info");
    g_message("some message");
    g_print("some print\n");
    g_printerr("some print error\n");
    g_debug("some debug");
    g_warning("some warning");
    g_error("some error");// This terminates the program.
}