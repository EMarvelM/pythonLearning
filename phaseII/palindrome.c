bool isPalindrome(int x){
    int y, copy;
    unsigned int z = 0;



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