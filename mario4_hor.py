#!/usr/bin/python3
"""
TRIANGLE
"""
j = 1
for i in range(4):
    k = 0
    for k in range(j):
        print("*", end="")
    j += 1

    print()


#print("?" * 4)


"""
RECTANGLE
"""
x = 3
for i in range(x):
    print("#" * x)

#OR

for i in range(x):
    for j in range(x):
        print("&", end="")
    print()