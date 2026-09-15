# Get a number from the user
day = int(input("Enter a number in the range 1 through 7: "))

# Check the number and display the day
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Error: Please enter a number in the range 1 through 7.")
