#!/usr/bin/python3

class Solution:
    def isPalindrome(x: int) -> bool:
        copy = x
        z = 0

        while True:
            y = x % 10
            x /= 10

            z *= 10
            z += y

            print(z)

            if x  == 0:
                if z == copy:
                    print("True")
                    return True
                else:
                    print("False")
                    return False

Solution.isPalindrome(4554)