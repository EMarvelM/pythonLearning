#!/usr/bin/python3

from sys import exit

lists = dict()
priority = []
yes = ["yes", "y"]
no = ["no", "n"]
prior = ["High", "Low", "Medium"]

def main():
    chosen = welcome()
    if chosen in yes:
        i = 0
        while True:
            new_title= input("Title: ")
            task = input("Description: ")
            while True:
                prio = input("Priority: ")
                prio = prio.capitalize()
                if prio in prior:
                    break

            priority.append(prio)
            if i == 0:
                lists = {new_title: task}
            else:
                lists[new_title] = task
            i = 1
            for title in lists:
                print()
                print(f"{i}. {title.upper()}:", f"priority: {priority[i - 1]}")
                print(" " * (len(title) + 5) + f"{lists[title]}", end="\n\n")
                i += 1



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