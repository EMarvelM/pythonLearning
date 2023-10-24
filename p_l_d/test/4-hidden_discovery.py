#!/usr/bin/python3
if __name__ == "__main__":
    import importlib

    hidden = importlib.import_module("hidden_4")
    hidden = dir(hidden)

    for i in range(len(hidden)):
        if hidden[i].startswith("__") == False:
            print(hidden[i])

