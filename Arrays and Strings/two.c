#include "stdio.h"
#include "string.h"

int main(int argc, char *argv[])
{
    char string[8] = "Hithere";
    /*printf("half %lu", strlen(string));*/
    for (int i = 0; i <= (int) (strlen(string)/2); ++i) {
        char *ptr = string + i; 
        char *last = string + strlen(string) - i - 1;

        char temp = *ptr;
        *ptr = *last;
        *last = temp;
        // Alternative method (3 XOR swap; no temp. vars)
        /**ptr ^= *last;*/
        /**last ^= *ptr;*/
        /**ptr ^= *last;*/
    }
    printf("%s\n", string);
    return 0;
}
