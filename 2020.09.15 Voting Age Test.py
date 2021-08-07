##########
# LV Marlowe
# 09/15/2020
# Voting Age Test
# This program asks the user's age and determines whether they are of voting age.
##########

# Ask for user's age.

age = input('How old are you?\n')  # string

# Notify user of invalid age and ask for age again.

while True:
    try:
        float(age)  # Try converting age to a float number.
    except ValueError:  # If age cannot be converted to a float number, it is invalid.
        print('Your age cannot contain letters or special characters.')  # Notify user of invalid age.
        age = input('How old are you?\n')  # Ask for user's age.
    else:
        if float(age) < 0:  # Determine if age is less than 0.
            print('Your age must be at least 0.')  # If so, inform user of invalid age.
            age = input('How old are you?\n')  # Ask for user's age.
        else:
            break  # Otherwise, stop loop.

# Determine whether user is of voting age and inform user.

if float(age) >= 18:  # Check if user is at least 18 years old.
    print('You are of voting age.')
else:  # Otherwise, user is under 18 years old.
    print('You must be 18 to vote.')
