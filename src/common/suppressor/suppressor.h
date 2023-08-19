#ifndef TESTING_SUPPRESSOR_H
#define TESTING_SUPPRESSOR_H

/*
 * Useful scripts for suppressing output to stdout
 * and stderr.
 * */

#include "error_codes/error_codes.h"

[[nodiscard]]
error_code suppressing_start(void);

[[nodiscard]]
error_code suppressing_stop(void);

#endif //TESTING_SUPPRESSOR_H
