#!/usr/bin/python3
a = 3
def _print():
    print("Hello world")

def _add():
    global a
    a = 3
    b = 5
    print(a + b)

# if we're runing from the terminal
if __name__ == "main":
    _print()
    _add()
