#!/usr/bin/python3

from sys import exit

lists = {}
priority = []
start = {
    "1": "add",
    "2": "remove",
    "3": "preview"
}
yes = ["yes", "y"]
no = ["no", "n"]
prior = ["High", "Low", "Medium"]

def main():
    chosen = welcome()
    if chosen in yes:
        i = 0
        while True:
            while True:
                new_title = input("Title: ")
                if new_title in start.values():
                    next(new_title, lists)
                if len(new_title) < 30:
                    break
                print("Title cannot be more than 30 characters")
            while True:
                task = input("Description: ")
                if len(task) > 5:
                    break
                print("Description too short\nTry again!")
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
        i = 1
        for title in lists:
            print(f"{i}. {title.capitalize()}:", end=" ")
            print(lists[title])
            i += 1
        return None

def next(check, lists):
    if check == "add":
        main()
    elif check == "remove":
        i = 1
        print("S/No" + " " * 3 + "TITLE" + " " * 35 + "DESCRIPTION")
        for new in lists:
            print(i, end=" " * 6)
            print(f"{new}", end=" " * (35 - len(new)))
            print(lists[new])
            i += 1

        j = 0
        remover = int(input("what task would you wanna remove? "))
        for lis in lists:
            j += 1
            if j == remover:
                lists[lis] = []#TODO: DELETE THE LIST


#def remove():
#def preview():

main()