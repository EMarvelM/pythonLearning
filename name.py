#!/usr/bin/python3
import sys

names = ["Marvel", "David", "Daniel", "Moses", "Micheal"]

name = input("What name would you wanna search for? ")

for n in names:
    if n == name:
        print(f"\"{name}\" found!")
        sys.exit(0)
    else:
        print(f"\"{name}\" was not found")
        sys.exit(1)