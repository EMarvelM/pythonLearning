#!/usr/bin/python3

for i in range(9):
    for j in range(1, 10):
        if j == i:
            continue
        if j < i:
            continue
        print(i, end = "")# i is ok

        if i == 8 and j == 9:
            print(j, end = "\n")
        else:
            print(j, end = ", ")