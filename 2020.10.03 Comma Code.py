##########
# LV Marlowe
# 10/03/2020
# Comma Code
# This program prints a grammatically correct list.
##########

# Start with an empty list to print.
listToPrint = []

while True:
    newWord = input('Enter a word to add to the list. Press "return" to stop adding words.\n')  # Instruct user how to add a new word to the list.
    if newWord == '':  # Check if user presses "return".
        break  # If so, stop asking for new words.
    else:
        listToPrint.append(newWord)  # Otherwise, add the new word to the list.

if len(listToPrint) == 0:  # Check if the list is empty.
    print('You didn\'t add any words to the list.')  # If so, tell the user.
elif len(listToPrint) == 1:  # Otherwise, check if the list is one word long.
    print(listToPrint[0])  # If so, print the list.
elif len(listToPrint) == 2:  # Otherwise, check if the list is two words long.
    print(listToPrint[0], 'and', listToPrint[1])  # If so, print both words separated by "and".
else:  # Otherwise, the list is more than two words long.
    for word in listToPrint[:-1]:  # So, print all except for the last word.
        print(word, end=', ')  # Separate those words with commas. Don't forget the Oxford comma; it enhances clarity and is patriotic.
    print('and', listToPrint[-1])  # Then, print "and" plus the last word in the list.
