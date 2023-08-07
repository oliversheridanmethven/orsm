#include "suppressor.h"
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

static int save_out;
static int save_err;
static int dev_null;

error_code suppressing_start(void) {

    if (fflush(stdout)) {
        fprintf(stderr, "Could not flush stdout.\n");
        return EC_FAILURE;
    }
    if (setvbuf(stdout, NULL, _IONBF, 0)) {
        fprintf(stderr, "Could not change the buffering of stdout.\n");
        return EC_FAILURE;
    }

    if (fflush(stderr)) {
        fprintf(stderr, "Could not flush stderr.\n");
        return EC_FAILURE;
    }
    if (setvbuf(stderr, NULL, _IONBF, 0)) {
        fprintf(stderr, "Could not change the buffering of stderr.\n");
        return EC_FAILURE;
    }

    save_out = dup(STDOUT_FILENO);
    if (save_out == -1) {
        fprintf(stderr, "Couldn't duplicate stdout.\n");
        return EC_FAILURE;
    }

    save_err = dup(STDERR_FILENO);
    if (save_err == -1) {
        fprintf(stderr, "Couldn't duplicate stderr.\n");
        return EC_FAILURE;
    }

    dev_null = open("/dev/null", O_WRONLY);
    if (dev_null == -1) {
        fprintf(stderr, "Error opening /dev/null'\n");
        return EC_FAILURE;
    }

    if (dup2(dev_null, STDOUT_FILENO) == -1) {
        fprintf(stderr, "Error in replacing (dup2) stdout.\n");
        return EC_FAILURE;
    }

    if (dup2(dev_null, STDERR_FILENO) == -1) {
        fprintf(stderr, "Error in replacing (dup2) stderr.\n");
        return EC_FAILURE;
    }

    return EC_SUCCESS;
}

error_code suppressing_stop(void) {

    if (dup2(save_out, STDOUT_FILENO) == -1) {
        fprintf(stderr, "Failed to swap back (dup2) the original stdout.\n");
        return EC_FAILURE;
    }

    if (dup2(save_err, STDERR_FILENO) == -1) {
        fprintf(stderr, "Failed to swap back (dup2) the original stderr.\n");
        return EC_FAILURE;
    }

    if (close(dev_null) == -1) {
        fprintf(stderr, "Failed to close dev_null.\n");
        return EC_FAILURE;
    }

    return EC_SUCCESS;
}
