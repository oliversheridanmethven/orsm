#include <stdio.h>
#include <string.h>
#include <regex.h>
#include "testing/testing.h"
#include "version/version.h"
#include "logging/logging.h"

Test(version, print_version) {
    printf("Version: %s\n", REPO_VERSION);
}

Test(version, not_dirty) {
    cr_expect(strstr(REPO_VERSION, "dirty") == nullptr, "We found the word \"dirty\" in the repository version " REPO_VERSION);
}

Test(version, contains_version) {
    cr_assert(strstr(REPO_VERSION, "v") != nullptr, "We could not find a \"v\" in the " REPO_NAME);
}

char * pattern = "^v[[:digit:]]\\{1,\\}[.][[:digit:]]\\{1,\\}[.][[:digit:]]\\{1,\\}.*";
regex_t regexp;
#define MAX_PATTERN 100
char good_patterns[][MAX_PATTERN] = {"v0.1.0", "v0.1.0-dirty", "v0.12.3"};
char bad_patterns[][MAX_PATTERN] = {"0.1.0", "v0.1", "v0..1", "v0.a.2"};

void setup_regexp(void) {
    // Function call to create regex
    if(regcomp(&regexp, pattern, 0)){
        LOG_ERROR("Could not compile regexp pattern: \"%s\"", pattern);
    }
}

Test(version, matches_pattern_successes, .init=setup_regexp) {
    for (size_t i = 0; i < sizeof(good_patterns) / sizeof(good_patterns[0]); i++)
    {
        char * good_pattern = good_patterns[i];
        switch(regexec(&regexp, good_pattern, 0, NULL, 0)) {
            case 0:
                LOG_INFO("Matched the pattern \"%s\" to %s", pattern, good_pattern);
                break;
            case REG_NOMATCH:
                LOG_ERROR("Could not match the pattern \"%s\" to %s", pattern, good_pattern);
                break;
            default:
                LOG_ERROR("An error occured trying to match the pattern: \"%s\" to %s", pattern, good_pattern);
                break;
        }
    }
}

Test(version, matches_pattern_failures, .init=setup_regexp) {
    for (size_t i = 0; i < sizeof(bad_patterns) / sizeof(bad_patterns[0]); i++)
    {
        char * bad_pattern = bad_patterns[i];
        switch(regexec(&regexp, bad_pattern, 0, NULL, 0)) {
            case 0:
                LOG_ERROR("Accidentally matched the pattern \"%s\" to %s", pattern, bad_pattern);
                break;
            case REG_NOMATCH:
                LOG_INFO("Did not match the pattern \"%s\" to the bad pattern %s", pattern, bad_pattern);
                break;
            default:
                LOG_ERROR("An error occured trying to match the pattern: \"%s\" to %s", pattern, bad_pattern);
                break;
        }
    }
}

Test(version, matches_pattern, .init=setup_regexp) {
    switch(regexec(&regexp, REPO_VERSION, 0, NULL, 0)) {
        case 0:
            LOG_INFO("Matched the pattern \"%s\" to %s", pattern, REPO_VERSION);
            break;
        case REG_NOMATCH:
            LOG_ERROR("Could not match the pattern \"%s\" to %s", pattern, REPO_VERSION);
            break;
        default:
            LOG_ERROR("An error occured trying to match the pattern: \"%s\" to %s", pattern, REPO_NAME);
            break;
    }

}
