#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    hidden_4 = importlib.import_module("hidden_4")
    hidden_4 = dir(hidden_4)

    for i in range(len(hidden_4)):
        if hidden_4[i][0] != "_" and hidden_4[i][1] != "_":
            print(hidden_4[i])
