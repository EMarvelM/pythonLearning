#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = -number
    number %= 10
    print(number, end="")
    return number

#    """TEST"""   #
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
