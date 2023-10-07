#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argv = sys.argv
    exit = sys.exit

    if len(argv) < 5:
        for i in range(len(argv)):# -1 to ignore the filename
            if i == 1:
                a = int(argv[i])
            elif i == 2:
                op = str(argv[i])
            elif i == 3:
                b = int(argv[i])
        print(a,b,op)
        if op == "+":
            result = calculator_1.add(a, b)
        elif op == "-":
            result = calculator_1.sub(a, b)
        elif op == "*":
            result = calculator_1.mul(a, b)
        elif op == "/":
            result = calculator_1.div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, result))
