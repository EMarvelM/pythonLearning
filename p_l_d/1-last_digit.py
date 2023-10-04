#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)

lnumber = number%10

print(f"Last digit of {number} is {lnumber:d} ")
if lnumber > 5:
    print("and is greater than 5")
elif lnumber == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")