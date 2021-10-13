#!/usr/bin/python3
"""Print the size of a square"""


def print_square(size):
    """Function square"""

    if not isinstance(size, (int)):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, (float)) and float < 0:
            raise TypeError("size must be an integer")
    
    for key in range(size):
        # The number typed in for the number of hashtags (columns)
        # is also the number for the rows
        # hence the for loop after the print
        [print("#", end="") for key in range(size)]
        print("")