#!/usr/bin/python3
import sys

names = ["Marvel", "David", "Daniel", "Moses", "Micheal"]

name = input("What name would you wanna search for? ")

#a search
for n in names:
    n = n.lower()
    name = name.lower()
    if n == name:
        print(f"\"{name}\" found!")
        sys.exit(0)
    else:
        print(f"\"{name}\" was not found")
        sys.exit(1)


#also same as
if name in names:
    print(f"\"{name}\" found!")
    sys.exit(0)

print(f"\"{name}\" was not found")
sys.exit(1)