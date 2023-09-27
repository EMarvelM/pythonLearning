#!/usr/bin/python3

from sys import exit

lists = dict()
priority = []
yes = ["yes", "y"]
no = ["no", "n"]
prior = ["High", "Low", "Medium"]

def main():
    chosen = welcome()
    



def welcome():
    print("\t\tTO-DO_LIST!")
    print()
    if len(lists) == 0:
        print("You currently don't a list in your task")
        while True:
            try:
                choose = input("Would you like to add one(Y/N)? ")
                choose = choose.lower()
                if choose in yes or choose in no:
                    break
                else:
                    print(f"Invalid input: '{choose}'")
            except ValueError:
                print("Invalid input")
        print()
        return choose
    else:
"""
        i = 1
        for title in lists:
            print(f"{i}. {title.capitalize()}:", end=" ")
            print(lists[title])
            i += 1
        return None
"""
        print(" what would you like to do? ")




main()