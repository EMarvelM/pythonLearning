def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        n = int(input("height: "))
        if (n > 0):
            return n

main()