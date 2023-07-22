#include <stdio.h>
#include "version.h"
#include "version/version.h"

int main(void) {
    printf("Version: %s\n", REPO_VERSION);
}
