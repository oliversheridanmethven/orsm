#ifndef TESTING_LOGGING_HPP
#define TESTING_LOGGING_HPP

#include <glog/logging.h> // The logging library of choice.

/* Some wrappers. */
#define LOG_INFO LOG(INFO)
#define LOG_DEBUG DLOG(INFO)
#define LOG_WARNING LOG(WARNING)
#define LOG_ERROR LOG(ERROR)

#define LOG_INIT(argv) google::InitGoogleLogging(argv[0]);

#endif //TESTING_LOGGING_HPP
