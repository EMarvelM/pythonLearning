"""
convert characters to upper case
"""
Before = input("Before: ")
print("After: ", end="")

#iterate through the users input
#this appears long not when i can uppercase a string
for c in Before:
    print(c.upper(), end="")
print()

"""
Alternatively
"""
#As simple as ABC
print(f"After: {Before.upper()}")