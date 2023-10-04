#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) == ord(" "):
            print(" ", end="")
        elif ord(c) in range(65, 91) or ord(c) in range(48, 58):
            print(chr(ord(c)), end="")
        elif ord(c) in range(97, 123):
            print(chr(ord(c) - (97 - 65)), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")