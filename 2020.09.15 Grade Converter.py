##########
# LV Marlowe
# 09/15/2020
# Grade Converter
# This program converts a grade percentage into a letter grade.
# Assume that fractions .5 and above are rounded up, fractions .4 and below are rounded down, and grade percentages below 0 are impossible.
##########

# Ask for user's grade percentage.

percentage = input('Enter your grade percentage to see your letter grade.\n')  # string

# Check if grade percentage is valid and ask for it again if it is invalid.

while True:
    try:
        float(percentage)  # Try converting grade percentage to a float number.
    except ValueError:  # If grade percentage cannot be converted, it is invalid.
        print('Your grade percentage cannot contain letters or special characters.')  # Inform user that grade percentage is invalid.
        percentage = input('Enter your grade percentage.\n')  # Ask for user's grade percentage.
    else:
        if float(percentage) < 0:  # Determine if grade percentage is less than 0.
            print('Your grade percentage must be at least 0.')  # If so, inform user that grade percentage is invalid.
            percentage = input('Enter your grade percentage.\n')  # Ask for user's grade percentage.
        else:
            break  # Otherwise, stop loop.

# Convert grade percentage into letter grade.

if float(percentage) >= 92.5:  # Check if grade percentage greater than or equal to 92.5.
    print('A')
elif 92.5 > float(percentage) >= 89.5:  # Check if grade percentage less than 92.5 and greater than or equal to 89.5.
    print('A-')
elif 89.5 > float(percentage) >= 86.5:  # Check if grade percentage less than 89.5 and greater than or equal to 86.5.
    print('B+')
elif 86.5 > float(percentage) >= 82.5:  # Check if grade percentage less than 86.5 and greater than or equal to 82.5.
    print('B')
elif 82.5 > float(percentage) >= 79.5:  # Check if grade percentage less than 82.5 and greater than or equal to 79.5.
    print('B-')
elif 79.5 > float(percentage) >= 76.5:  # Check if grade percentage less than 79.5 and greater than or equal to 76.5.
    print('C+')
elif 76.5 > float(percentage) >= 72.5:  # Check if grade percentage less than 76.5 and greater than or equal to 72.5.
    print('C')
elif 72.5 > float(percentage) >= 69.5:  # Check if grade percentage less than 72.5 and greater than or equal to 69.5.
    print('C-')
elif 69.5 > float(percentage) >= 66.5:  # Check if grade percentage less than 69.5 and greater than or equal to 66.5.
    print('D+')
elif 66.5 > float(percentage) >= 62.5:  # Check if grade percentage less than 66.5 and greater than or equal to 62.5.
    print('D')
elif 62.5 > float(percentage) >= 59.5:  # Check if grade percentage less than 62.5 and greater than or equal to 59.5.
    print('D-')
else:  # Otherwise, grade percentage is less than 59.5 and greater than or equal to 0.
    print('F')
