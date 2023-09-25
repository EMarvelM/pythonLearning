x = int(input("input a number: "))

if x > 10:
    print(str(x) + " is greater than 10")
elif x < 10:
    print(f"{x} is less than 10")
else:
    print(x, "is 10")