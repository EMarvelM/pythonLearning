import cmd

class Todo(cmd.Cmd):
    prompt = "(ToDoList): "

    def do_prompt(self, prompt):
        """ Set the prompt message """
        if prompt:
            _prompts = prompt.split()
            if len(_prompts) > 1:
                print("** Too many arguments **")
            else:
                prompt += ":" if prompt[-1] != ":" else None
                prompt += " " if prompt[-1] != " " else None
                self.prompt = prompt
        else:
            print("** Missing Argument **")



if __name__ == "__main__":
    Todo().cmdloop()
