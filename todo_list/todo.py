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

            todo_list.save()
        else:
            print("** Missing Task **\nUsage: add task_title")

if __name__ == "__main__":
    Todo().cmdloop()
