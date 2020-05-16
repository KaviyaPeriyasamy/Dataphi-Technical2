#include <stdio.h>
int strcmp(char* src,char* dest)
{
    int i;
    // iterate until it reaches null value.
    for (i=0; src[i]!=0 || dest[i]!=0; i++)
    {
        // Here it compares the ascii values of the compared characters.
        if (src[i] > dest[i])
            return 1;
        if (src[i] < dest[i])
            return -1;
    }
    return 0;
}
int main()
{
    // char src[] = "ABC";
    // char dest[] = "DEF";
    char src[] = {'E','F'};
    char dest[] = {'E','G'};
    int result= strcmp( src, dest);
    printf("%d",result);
    return 0;
}
