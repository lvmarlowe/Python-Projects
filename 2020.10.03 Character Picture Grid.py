##########
# LV Marlowe
# 10/03/2020
# Character Picture Grid
# This program uses a grid of characters to print a picture.
##########

# Define the grid.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Print the picture.

for column in range(0, 6):  # For each coordinate in a column in the range of 0 through 6,
    for row in range(0, 9):  # And for each coordinate in a row in the range of 0 through 9,
        print(grid[row][column], end='')  # Print the character at that coordinate.
    print()  # Start new line for set of characters using next column coordinate in sequence.
