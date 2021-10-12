#!/usr/bin/python3
"""Print the size of a square"""

def print_square(size):

    if not isinstance(size, (int)):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, (float)) and float < 0:
            raise TypeError("size must be an integer")
    
    for key in range(size):
        print("#", end="")
        print("")