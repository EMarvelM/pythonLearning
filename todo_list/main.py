# print("/" * 10, "TODO - LIST", "\\" * 10, end = "\n\n")
""" Create a empty list """
todo_list = []

while True:
    print("\n"*3, "=" *10, "TODO - LIST", "="*10, end="\n\n")

    print("What would you like to do?")
    print("1. Add to list of tasks")
    print("2. Delete from list of tasks")
    print("3. View list of tasks")

    choice = input("Input Here: ").lower()

    if choice in ["1", "add", "add to list", "1."]:
        # code to process input to a task
        task = input("What's your task:: ")
        if task == "":
            print("Invalid input")
        else:
            todo_list.append(task)

    elif choice in ["2", "2.", "delete", "delete from list"]:
        # print all in the todo_list in number
        if todo_list == []:
            print("is an empty list")
        else:
            i = 1
            for eachItem in todo_list:
                print(str(i) + ".", eachItem)
                i = i + 1
            
            deleting = int(input(f"Choose from the list above (1 - {i-1}) "))
            if deleting < i or deleting > 0:
                del(todo_list[deleting - 1])
            else:
                print("Out of Range")
        # ask the user to choose from list
        # delete a particular item from the list

    elif choice in ["3", "3.", "view", "view list"]:
        # code to display the list
        if todo_list is not None:
            print("\n\t == TODOLIST ==")
            # for each item in the list print them
            for each_item in todo_list:
                print("\t:: " + each_item)

    else:
        print(" Invalid input ")
        print("= Try Again! =")
