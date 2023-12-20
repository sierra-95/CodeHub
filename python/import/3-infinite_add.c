#include <stdio.h>
#include <stdlib.h>
int main(int ac, char **av)
{
    int sum=0;
    int i;
    printf("Arguments: %d \n",ac-1);
    printf("Filename: %s \n",av[ac*0]);
    for (i=1;i<ac;i++)
    {
        printf("%d: %s \n",i,av[i]);
        sum+=atoi(av[i]);
    }
    printf("sum=%d \n",sum);
    return 0;
    

}