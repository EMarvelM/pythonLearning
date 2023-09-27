#!/usr/bin/python3
import sys

j = 8
x = 5.0
n = 5.0j
names = ["Marvel", "Martins"]#list
dic = {
    "name": "Marvel",
    "status": "Learning"
}#dict
fruits = ("apple", "banana", "cherry")#tuple
names = {"Martins", "Emmanuel", "Samuel", "Marvel"}#set
name_lists = ["Marvel", "Samuel", "Martins", "Emmanuel"]



print(f"j is    {type(j)}")
print(f"x is    {type(x)}")
print(f"n is    {type(n)}")
print(f"name is {type(names)}")

for se in name_lists:
    print(se, end=" ")
print()
suggest = input("What name do you think would come first out of the above names: ")

i = 0
for see in names:
    if i == 0 and suggest == see:
        print("Correct!")
        sys.exit(0)
        i += 1

    else:
        print("Wrong!\nTry Again")
        sys.exit(1)