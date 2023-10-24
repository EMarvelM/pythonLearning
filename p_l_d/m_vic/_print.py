#!/usr/bin/python3

import pract

taken = input("Input a operator: ")
print()#prone to be removed: for test

lis = ['+', '-', '/', '*']
checkp = ""
ans = []
var = []
reset = 0
op = []

for c in taken:
    if c in lis:
        op += [c]
        for val in var:
            checkp += val
        ans += [int(checkp)]
        var.clear()
        checkp = '' #reset point
        continue

    if c == ' ':
        continue
    if int(c) in range(10):
        var += list(c)

var = [int(var[0])]
ans += var
print(ans)
print(op)

answer:float = ans[0]
#AND IN THE END...#
for i in range(len(ans) - 1):
    if op[i] == '+':
        if i == 0:
            continue
        answer += ans[i]

print(answer)

#lemme know when youre back
#module, object, __init__, method,