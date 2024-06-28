# Write a Python program that prompts the user to enter a number corresponding to a month (1 for January, 2 for February, ..., 12 for December). The program should then display the name of the month based on the number entered.
no_of_month = int(input("Enter no of month[1-12]: "))

if no_of_month == 1:
    print("The Month is January")
elif no_of_month == 2:
    print(" The Month is February")
elif no_of_month ==3:
    print("The Month is March")
elif no_of_month ==4:
    print("The Month is April")
elif no_of_month == 5:
    print("The Month is May")
elif no_of_month == 6:
    print("The Month is June")
elif no_of_month == 7:
    print("The Month is July")
elif no_of_month == 8:
    print("The Month is August")
elif no_of_month == 9:
    print("The Month is September")
elif no_of_month == 10:
    print("The Month is October")
elif no_of_month == 11:
    print("The Month is November")
elif no_of_month == 12:
    print("The Month is December")
else:
    print("invalid")