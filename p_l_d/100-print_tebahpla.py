#!/usr/bin/python3
# while True:
for i in reversed(range(65, 91)):
    if i % 2 == 1:
        print(chr(i), end="")
    elif i % 2 == 0:
        print(chr(97 - 65 + i), end="")