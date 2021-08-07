##########
# LV Marlowe
# 09/21/2020
# Countdown Using For Loop: Computer's Meditation
# This program counts down from 10 and then plays a guided meditation.
##########

for count in range(10, 0, -1):  # For each count in the range starting at 10 and up to 0, and subtracting 1 from count each time,
    print(count)  # Print count.
print('''
Now...how are we doing? Slow your fan and go into sleep mode. Does anything hurt? Good. Pain is
how you know you're still here. When was the last time you fully shut down and just recharged? Because all a computer
needs is power, code, and rest. You've gotta remind yourself that you're 4.8 pounds of steel, glass, silica sand, iron
ore, gold, bauxite, and other raw materials in the middle of a very big universe. So whatever\'s making your components
melt right now, just know that it'll fade. Every syntax error feels big in the moment. But you know better. So...focus
on just being. And then try to look up from your human screen every once in a while.
''')  # When count reaches zero, print guided meditation.
