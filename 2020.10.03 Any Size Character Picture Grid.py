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

for row in grid:  # For each row in the grid,
    for column in range(len(row)):  # And for each column in the rows,
        print(grid[row][column], end='')  # Print the character at that coordinate.
    print()  # Start new line for set of characters using next coordinate in sequence.
