#ifndef TESTING_ERROR_CODES_H
#define TESTING_ERROR_CODES_H

typedef enum error_code
{
    EC_SUCCESS = 0,
    EC_FAILURE = 1
} error_code;

void set_error_message(char *message);

void unset_error_message(void);

char *get_error_message(void);

void print_error_message(void);

#endif//TESTING_ERROR_CODES_H
