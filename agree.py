"""
answer = input("Do you agree(Y/N)? ")
if answer.lower() == 'y':
    print("Agreed")
elif answer.lower() == 'n':
    print("Not Agreed")
else:
    print("Not understood")

#OR

answer = input("Do you agree(Y/N)? ")
if answer == 'y' or answer == 'Y':
    print("Agreed")
elif answer == 'n' or answer == 'N':
    print("Not Agreed")
else:
    print("Not understood")
"""
#OR

answer = input("Do you agree(Y/N)? ")
answer = answer.lower()

if answer in ["y", "yes"]:
    print("Agreed")
elif answer in ["n", "No"]:
    print("Not Agreed")
else:
    print("Not Understood")