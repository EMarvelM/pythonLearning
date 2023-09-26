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

    writer = csv.writer(file)
    writer.writerow([Name, Number])
    file.close()


file.close()
exit(1)