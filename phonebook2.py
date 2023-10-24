#!/usr/bin/python3
import csv
from sys import exit


while True:
    file = open("phonebook2.csv", "a")
    Name = input("Name: ")
    Number = input("Number: ")
    #just press enter to exit
    if Name == '':
        file.close()
        exit(0)

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": Name,"number": Number})
    file.close()


file.close()
exit(1)

"""
You can avoid worrying about closing the file and just use the
with open(filename) as file:
file is a variable hear
"""
"""
with open("phonebook2.py", "a") as file:
    name = input("Name: ")
    number = input("Number:")

    writer = csv.writer(file)
    writer.writerow([name, number])
"""