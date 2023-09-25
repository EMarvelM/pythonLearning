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

#OR

answer = input("Do you agree(Y/N)? ")
if answer in ["Y", "y"]:
    print("Agreed")
elif answer in ["N", 'n']:
    print("Not Agreed")
else:
    print("Not Understood")