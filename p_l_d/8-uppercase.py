#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) == ord(" "):
            print(" ", end="")

        elif ord(c) in range(97, 123):
            print(chr(ord(c) - (97 - 65)), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")