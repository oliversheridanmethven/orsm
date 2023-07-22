#ifndef TESTING_H_
#define TESTING_H_

#include <criterion/criterion.h>

#define EXPECT(condition, ...) cr_expect((condition), __VA_ARGS__)

#endif /*TESTING_H_*/
