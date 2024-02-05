#!/usr/bin/env python3
"""Todo list Interpreter"""

import cmd
from engine import TodoObject

class Todo(cmd.Cmd):
    prompt = "(ToDoList): "


    def do_prompt(self, prompt):
        """ Set the prompt message """
        if prompt:
            _prompts = prompt.split()
            if len(_prompts) > 1:
                print("** Too many arguments **")
            else:
                prompt += ":" if prompt[-1] != ":" and prompt[-2] != ":" else None
                prompt += " " if prompt[-1] != " " else None
                self.prompt = prompt
        else:
            print("** Missing Argument **")

    def do_add(self, task):
        """Add a new task to the todo_list"""
        if task:
            todo_list = TodoObject(task)
            todo_list.description = input("Enter Description: ")
            print("\nChoose from the priority")
            while True:
                priority = input("High(H), Medium(M) Low(L)::: ").lower()
                if priority in ["high", "h", "low", "l", "medium", "m"]:
                    todo_list.priority = priority
                    break
                else:
                    print("** Invalid selection **\n")

            todo_list.save()  # save the informations
        else:
            print("** Missing Task **\nUsage: add task_title")

    def do_view(self, task):
        todo_list = TodoObject()
        if not task:
            print(" " + "=" * 50)
            print("|\t Title\t\t|\tDescription\t","|")
            print(" " + "=" * 50, end="\n")
            for data in todo_list._object:
                # //TODO// if description is greater than certain length of text use double \t
                print(f'|\t {data["title"]} \t\t|\t {data["description"]}\t |')
                print(" " + "-" * 50)
        elif task:
            tasks = task.split()
            for t in tasks:
                if t in [i["title"]for i in todo_list._object] or t in [str(i["off_set"]) for i in todo_list._object]:
                    for j in todo_list._object:
                            if j["title"] == t or str(j["off_set"]) == t:
                                print(" " + "-" * 50)
                                print(f'|\t{j["title"]} \t\t|\t {j["description"]}\t |')
                                print(" " + "-" * 50)
                else:
                    print(f"** '{t}' not found **")

    def do_remove(self, task):
        if not task:
            self.do_view(None)


if __name__ == "__main__":
    Todo().cmdloop()
