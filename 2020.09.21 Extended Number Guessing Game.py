##########
# LV Marlowe
# 09/21/2020
# Extended Number Guessing Game
# This program plays an extended number guessing game with the user.
##########

# Select random number from 1 to 100.

from random import randint
randomNum = randint(1, 100)  # integer

# Ask user to guess number from 1 to 100.

guess = input('I\'m thinking of a number from 1 to 100.\nGuess my number.\n')

# Check validity and correctness of guess and inform user.

while True:
    try:
        int(guess)  # Try converting guess to an integer.
    except ValueError:  # If guess cannot be converted, it is invalid.
        print('Your guess cannot contain letters or special characters.')  # Notify user that guess is invalid.
        guess = input('Guess my number.\n')  # Ask user to guess number.
    else:
        if not 1 <= int(guess) <= 100:  # Check if guess is from 1 to 100.
            print('Your guess must be from 1 to 100.')  # Notify user that guess is invalid.
            guess = input('Guess my number.\n')  # Ask user to guess number.
        else:
            if int(guess) > randomNum:  # Check if guess higher than number.
                print('My number is lower than', guess + '.')  # Notify user that guess is too high.
                guess = input('Guess again.\n')  # Tell user to guess again.
            elif int(guess) < randomNum:  # Check if guess lower than number.
                print('My number is higher than', guess + '.')  # Notify user that guess is too low.
                guess = input('Guess again.\n')  # Tell user to guess again.
            else:  # Otherwise, guess is correct.
                print('Congrats! You guessed my number!')  # Notify user that guess is correct.
                break  # Stop loop.
