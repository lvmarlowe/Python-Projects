##########
# LV Marlowe
# 09/15/2020
# Calculator
# This program adds two numbers with a sum of 100 or less.
##########

# Ask for first number.

firstNum = input('Enter a number.\n')  # string

# Check if first number is valid and ask for it again if it is invalid.

while True:
    try:
        float(firstNum)  # Try converting first number to a float number.
    except ValueError:  # If first number cannot be converted, it is invalid.
        print('Your number cannot contain letters or special characters.')  # Inform user that first number is invalid.
        firstNum = input('Enter a number.\n')  # Ask for first number.
    else:
        break  # Otherwise, stop loop.

# Ask for second number.

secondNum = input('Enter another number.\n')  # string

# Check if second number is valid and ask for it again if it is invalid.

while True:
    try:
        float(secondNum)  # Try converting second number to a float number.
    except ValueError:  # If second number cannot be converted, it is invalid.
        print('Your number cannot contain letters or special characters.')  # Inform user that second number is invalid.
        secondNum = input('Enter another number.\n')  # Ask for second number.
    else:
        break  # Otherwise, stop loop.

# Determine whether sum of both numbers is 100 or less.

total = float(firstNum) + float(secondNum)  # float
if total <= 100:  # Check if sum of first number and second number is 100 or less.
    print('They add up to', str(total) + '.')  # Calculate, convert to string to end with period not proceeded by period, and inform user of sum.
else:
    print('They add up to a big number.')  # Otherwise, inform user that the two numbers add up to a big number.
