#include <stdbool.h>
bool isPalindrome(int x);

int main(void)
{
    
}

bool isPalindrome(int x){
    int y, copy;
    unsigned int z = 0;

    if (x < 0)
        return (false);
    copy = x;

    while (1)
    {
        y = x % 10;
        x /= 10;

        z = z * 10;
        z += y;

        if (x == 0)
                if (z == copy)
                    return (true);
                else
                    return (false);
    }
}