#!/usr/bin/python3

for i in range(99):
    if i < 10:
        print(f"{0:d}", end="")
    print(f"{i:d},", end=" ")
    if i == 98:
        print(99)
