#include <stdio.h>
#include <stdlib.h>
int romanToInt(char * s);

/**
 * main - Entry point.
 *
 * Return: 0 always on sucess
*/
int main(void)
{
    romanToInt("III");

    return (0);
}

int romanToInt(char * s){
    /*check the values*/
    int i = 0, j, valid = -1;

    char roman[] = "IVXLCDM";

    while (s[i])
    {
        for (j = 0; roman[j] != '\0'; j++)
        {
            if (s[i] == roman[j])
            {
                valid = 0;
                /*printf("%c  ", s[i]);
                printf("%c\n", roman[j]);*/
            }
        }
        if (valid == -1)
        {
            exit(1);
        }
        valid = -1;
        i++;
    }
    if (i > 15)
    {
        exit(1);
    }

    return (i);
}
