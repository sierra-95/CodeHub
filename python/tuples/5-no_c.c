#include <stdio.h>
#include <string.h>
int main()
{
    char str[]="michael";
    int i;
    for (i=0; i< strlen(str); i++)
    {
        if (str[i] != 99 && str[i] != 67)
        {
            printf("%c",str[i]);
        }
    }
    putchar('\n');
}