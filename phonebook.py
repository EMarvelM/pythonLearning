#!/usr/bin/python3
contact = {
    "Marvel": "+234-808 3340 791",
    "Martins": "+234-902 2690 343"
}

name = input("What name would you like to search for: ")

if name in contact:
    print(contact[name])