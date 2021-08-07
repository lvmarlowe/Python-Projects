##########
# LV Marlowe
# 09/15/2020
# Number Guessing Game
# This program plays a number guessing game with the user.
##########

# Select random number from 0 to 9.

from random import randint
randomNum = randint(0, 9)  # integer

# Ask user to guess number from 0 to 9.

guess = input('I\'m thinking of a number from 0 to 9.\nGuess my number.\n')

# Check validity and correctness of guess and inform user.

while True:
    try:
        int(guess)  # Try converting guess to an integer.
    except ValueError:  # If guess cannot be converted, it is invalid.
        print('Your guess cannot contain letters or special characters.')  # Notify user that guess is invalid.
        guess = input('Guess my number.\n')  # Ask user to guess number from 0 to 9.
    else:
        if not 0 <= int(guess) <= 9:  # Check if guess is from 0 to 9.
            print('Your guess must be from 0 to 9.')  # Notify user that guess is invalid.
            guess = input('Guess my number.\n')  # Ask user to guess number from 0 to 9.
        else:
            if int(guess) is not randomNum:  # Check if guess is incorrect.
                print('That is not my number.')  # Notify user that guess is incorrect.
                guess = input('Guess again.\n')  # Tell user to guess again.
            else:  # Otherwise, guess is correct.
                print('Congrats! You guessed my number!')  # Notify user that guess is correct.
                break  # Stop loop.
