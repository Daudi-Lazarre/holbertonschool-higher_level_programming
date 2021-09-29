#!/usr/bin/python3

# I'm not sure I understand this at the moment, but hey...
# Ask C15 about this tomorrow

# MY UNDERSTANDING:
# Increment through 0-8
# and also (first + 1) up until the the number 9
# print both digits with a comma and space
# print 89, but not 99 

for first in range(0, 8):
    for second in range(first + 1, 10):
        print("{:d}{:d}".format(first, second), end=', ')
print("{:d}{:d}".format(first + 1, second))
