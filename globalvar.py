# declaring a global variable
x = 5

#written my first function: looks cool🆒
def func():
    x = 6
    print(x + 1)

print (x + 1)

func()


name = "Unknown"

def myfun():
    global name
#after been declared changed the name of a global variable
    name = "EMarvel"

myfun()

# print the global variable declared in the function
print(name)