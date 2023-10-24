#!/usr/bin/python3
from sys import argv

if len(argv) > 1:
    if len(argv) == 2:
        print("{0:d} argument:".format(len(argv) - 1))
    else:
        print("{0:d} arguments:".format(len(argv) - 1))
else:
    print("{0:d} arguments.".format(len(argv) - 1))

#print the list of arguments
for i in range(len(argv) - 1):
    print(i + 1, end=": ")
    print(argv[i + 1])
