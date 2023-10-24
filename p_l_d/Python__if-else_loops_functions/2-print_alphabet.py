#!/usr/bin/python3
x: int = ord("a")
while True:
    print(chr(x), end = "")
    x += 1
    #break at 'z'
    if x >= 123:
        break
