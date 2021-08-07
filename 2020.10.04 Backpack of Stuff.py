##########
# LV Marlowe
# 10/04/2020
# Backpack of Stuff
# This program adds and inventories the contents of the backpack.
##########

# Import system-specific parameters and functions.

import sys

# List the items already in the backpack.

itemsInBackpack = ['book', 'computer', 'keys', 'travel mug']

# Ask what user would like to do.

while True:
    print('Would you like to:')
    print('1. Add an item to the backpack?')
    print('2. Check if an item is in the backpack?')
    print('3. Quit?')
    userChoice = input()

# Perform selected task.

    if userChoice == '1':  # Check if user wants to add an item to the backpack.
        itemToAdd = input('\nWhat do you want to add to the backpack?\n')  # If so, ask what the item is.
        itemsInBackpack.append(itemToAdd)  # Add item to list of items in backpack.
        print('You have added your', itemToAdd, 'to the backpack.\n')  # Notify user that item was added.

    if userChoice == '2':  # Check if user wants to check if an item is in the backpack.
        itemToCheck = input('\nWhat item do you want to check the backpack for?\n')  # If so, ask what the item is.
        if itemToCheck in itemsInBackpack:  # Check if the item is in the backpack.
            print('Yes, your', itemToCheck, 'is/are in the backpack.\n')  # If so, notify user that item is in the backpack.
        else:  # Otherwise, the item is not in the backpack.
            print('No, your', itemToCheck, 'is/are not in the backpack.\n')  # So, notify user that item is not in the backpack.

    if userChoice == "3":  # Check if user wants to quit.
        sys.exit()  # If so, exit the program.
