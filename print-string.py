#!/usr/bin/python3
str = "Holberton School"
print(str + str + str)
try:
    print(f"{9:str}")#trying to print from begining till 9th letter
except ValueError:
    print("Error on line:5")