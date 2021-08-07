##########
# LV Marlowe
# 10/15/2020
# Password Saver
# This program:
    # 1. Opens the password file,
    # 2. Looks up passwords for websites,
    # 3. Adds new passwords for websites,
    # 4. Saves website passwords to a file,
    # 5. Prints a list of websites and corresponding encrypted passwords, and
    # 6. Deletes saved websites and corresponding passwords.
##########

# Import system-specific parameters and functions and comma-separated values.

import csv
import sys

# Set starting values.

passwords = [['yahoo','XqffoZeo'],['google','CoIushujSetu']]  # Starting password list.
passwordFileName = 'samplePasswordFile'  # Password file name.
encryptionKey = 16  # Encryption key for Caesar Cypher.

# Set up Caesar Cypher Encryption.

def passwordEncrypt (unencryptedMessage, encryptionKey):

    encryptedMessage = ''  # Set encryptedMessage to an empty string.

    for symbol in unencryptedMessage:  # For each symbol in unencryptedMessage, add an encrypted symbol into the encryptedMessage.
        if symbol.isalpha():
            num = ord(symbol)
            num += encryptionKey

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

# Set up loading password file.

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

# Set up saving password file.

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)

# Set up repeating prompt.

while True:
    print('What would you like to do:')
    print(' 1. Open the password file.')
    print(' 2. Look up a password.')
    print(' 3. Add a password.')
    print(' 4. Save the password file.')
    print(' 5. Print the encrypted password list (for testing).')
    print(' 6. Delete a password.')
    print(' 7. Quit the program.')
    choice = input('Please enter a number (1-7).\n')

    if(choice == '1'):  # Check if user chose to load the password file.
        passwords = loadPasswordFile(passwordFileName)  # If so, load the password file and refer to it as "passwords".
        print('Your password file has been loaded.')  # Notify user that password file loaded.

    if(choice == '2'):  # Check if user chose to look up a password.
        print('Which website do you want to look up the password for?')  # Ask user to chose website from list.
        for keyvalue in passwords:  # For every entry in the password file,
            print(keyvalue[0])  # Print the website name.
        passwordToLookUp = input().lower()  # Convert input to lowercase.

        for i in range(len(passwords)):
            if passwordToLookUp in passwords[i][0]:
                print('Your password for', passwordToLookUp, 'is:', passwordEncrypt (passwords[i][1], -encryptionKey))

    if(choice == '3'):  # Check if user chose to add a password.
        website = input('Which website is this password for?\n').lower()  # Ask user for website to add password for.
        unencryptedPassword = input('What is the password?\n')  # User's input is the corresponding unencrypted password.
        encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)  # Encrypt the corresponding password.
        keyvalueToAdd = [website, encryptedPassword] # The name of the website and the corresponding encrypted password is what will be added.
        passwords.append(keyvalueToAdd)  # Add them to password file.
        print('Your password for', website, 'has been added.')  # Notify user that password added.

    if(choice == '4'):  # Check if user chose to save the password file.
        savePasswordFile(passwords, passwordFileName)  # If so, save password file.
        print('Your password file has been saved.')  # Notify user that password file saved.

    if(choice == '5'):  # Check if user chose to print the encrypted password list.
        for keyvalue in passwords:  # For every entry in the password file,
            print(', '.join(keyvalue))  # Print the website and corresponding encrypted password.

    if(choice == '6'):  # Check if user chose to delete a password.
        print('Which website do you want to delete the password to?')
        for keyvalue in passwords:  # For every entry in the password file,
            print(keyvalue[0])  # Print website name.
        websiteToDelete = input().lower()  # The user's input converted to lowercase is the website to delete.
        for keyvalue in passwords:  # For every entry in the password file,
            if websiteToDelete in keyvalue:  # Check if the website to delete appears.
                passwords.remove(keyvalue)  # If so, remove the website name and corresponding password.
                print('Your password has been deleted.')  # Notify user that password deleted.
                break  # Stop loop.
        else:  # Otherwise, user has entered a website not in the password file.
            print('You have not saved a password for', websiteToDelete + '.')  # Notify user that there is no entry for the website entered.

    if(choice == '7'):  # Check if user chose to exit the program.
        sys.exit()  # If so, exit the program.

    print()  # Print a blank line.
