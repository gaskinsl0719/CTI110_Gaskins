# CTI-110
# P4Lab1- Part B
# Text "graphics"
# GaskinsL
# 10/5/23

# Draw a rectangle with text
CHAR = "$"
#print(CHAR)

# PArt 1: Draw a horizontal line
WIDTH = 9
HEIGHT = 9
"""print("printing", WIDTH, "columns")
for column in range(WIDTH):
    # dont go to newline
    print(CHAR, end="")
# Part 2: Vertical line
for row in range(HEIGHT):
    print(CHAR) # we want the newline
"""
# Part 3: Draw the rectangle

for row in range(HEIGHT):
    for column in range(WIDTH):
        print(CHAR, end="")
    print() # end the line