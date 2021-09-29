#!/usr/bin/python3

# SMH, I want to use a list comprehension.
# I can't though, because Holberton.
# oneToNinetyNine = [num for num in range(1, 99)]
# print(oneToNinetyNine)

# For the numbers from 0 to 99
# Print, using two places, the numbers
# end the printed statement with a comma and space
# Then, once that is done, print the number 99

for num in range(0, 99):
    print("{:02d}".format(num), end=", ")
print("{:02d}".format(num + 1))
