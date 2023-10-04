#!/usr/bin/python3
x: int = ord("a")
while True:
    if x is not ord("q") and x is not ord("e"):
        print(chr(x), end = "")
    x += 1
    #break at 'z'
    if x >= 123:
        break
