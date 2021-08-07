##########
# LV Marlowe
# 09/20/2020
# Multiplication Table
# This program prints a multiplication table for numbers 1 through 9.
##########

for firstNum in range(1, 10):  # For each first number in the range starting at 1 and up to 10,
    for secondNum in range(1, 10):  # And for each second number in the range starting at 1 and up to 10,
        total = (firstNum * secondNum)  # Calculate the total as the first number times the second number.
        print(str(total).rjust(2), end='\t')  # Convert total to string to print right-justified total, and add tab instead of new line between totals calculated using same first number.
    print()  # Start new line for set of totals calculated using next first number in sequence.
