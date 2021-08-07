##########
# LV Marlowe
# 09/21/2020
# Binary Counting
# This program tells user how high they can count on n number of fingers using the binary method.
##########

for n in range(1, 2):  # For when n equals 1,
    print('On', n, 'finger, you can count to', str(2**n) + '.')  # Calculate 2**1, convert total to string to end with period not proceeded by space, and print how high user can count on 1 finger.
for n in range(2, 101):  # For each value of n in the range starting at 2 and up to 101,
    print('On', n, 'fingers, you can count to', str(2**n) + '.')  # Calculate 2**n, convert total to string to end with period not proceeded by space, and print how high user can count on n fingers.
