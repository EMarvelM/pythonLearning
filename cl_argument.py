#!/usr/bin/python3
from sys import argv

if len(argv) > 1:
    for i in range(len(argv) - 1):#minus 1 to avoid counting the argv[0]
        if i == 0:
            print("Hello ", end="")
        print(f"{argv[i + 1]}", end=" ")#added 1 to start interating from 1 not 0

else:
    print("Hello World")