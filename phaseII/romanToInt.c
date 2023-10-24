#include <stdio.h>
#include <stdlib.h>
unsigned int romanToInt(char * s);

/**
 * main - Entry point.
 *
 * Return: 0 always on sucess
*/
int main(void)
{
    unsigned int total;

    total = romanToInt("MCMXCIV");

    printf("%d\n", total);

    return (0);
}

unsigned int romanToInt(char * s){
    /*check the values*/
    int i = 0, j, valid = 2;
    /*int a_I, a_V, a_X, a_L, a_C, a_D, a_M;*/
    unsigned int total = 0;

    char roman[] = "IVXLCDM";

    while (s[i])
    {
        for (j = 0; roman[j] != '\0'; j++)
        {

            /*test*/
            printf("%c  %c\n", s[i], roman[j]);

            valid += 1;
            switch (s[i]){
                case 'M':
                {
                    total += 1000;
                }
                break;

                case 'C':
                if (s[i + 1] == 'M')
                {
                    total += 900;
                    i += 2;
                    valid++;
                }
                else
                    total += 100;
                break;

                case 'X':
                if (s[i + 1] == 'C')
                {
                    total += 90;
                    i += 2;
                    valid++;
                }
                else
                    total += 10;
                break;

                case 'I':
                if (s[i + 1] == 'X')
                {
                    total += 9;
                    i += 2;
                    valid++;
                }
                else if (s[i + 1] == 'V')
                {
                    total += 4;
                    i += 2;
                    valid++;
                }
                else
                    total += 1;
                break;

                default:
                exit(1);
                break;
            }

        }
        i++;
    }
    if (i > 15)
    {
        exit(1);
    }

    return (total);
}

