"""
Multi variable name
"""
#camel case
myVariableName = "Testing"
#pascal case
MyVariableName = "Testing"
#snake case
my_variable_name = "Testing"


"""
Assigning multi variables
"""
x, y, z = "First", "Second", "Last"
#be sure number of variables match number of values to assign
print(x)
print(y)
print(z)

"""
Assigning one value to different variables
"""
x = y = z = "All the same"
print(x)
print(y)
print(z)

"""
unpacking values to variables
"""
colection = ["This", "is", "list"]
x, y, z = colection
#this will have a newline at the middle
print(x)
print(y)
print(z)
colection = {"This", "is", "tuple"}#always random lolz
x, y, z = colection
print(x, y, z)#this will not have a newline at the middle
