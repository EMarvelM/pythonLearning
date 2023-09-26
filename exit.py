import sys

#if the user does type a command line argument
if len(sys.argv) < 2:
    print("Your missing an argument!")
    sys.exit(1)
else:
    print(f"Hello {sys.argv[1]}")
    sys.exit(0)