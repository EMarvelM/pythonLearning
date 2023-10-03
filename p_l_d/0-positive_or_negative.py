#!/usr/bin/python3
from random import randint

x = randint(-100, 100)
if x > 0:
    print(f"{x:d} is positive")
elif x < 0:
    print(f"{x:d} is negative")
else:
    print(f"{x:d} is zero")