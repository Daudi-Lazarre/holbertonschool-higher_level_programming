#!/usr/bin/python3
for first in range(0, 9):
    for second in range(first + 1, 10):
        print("{:d}{:d}".format(first, second), end=', ')
print("{:d}{:d}".format(first + 1, second))
