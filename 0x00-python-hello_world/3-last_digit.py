#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Case for positive numbers
if number > 0:
    positiveDigit = number % 10
    print("Last digit of " + str(number) +  " is " + str(positiveDigit))
    if positiveDigit > 5:
        print("and is greater than 5")
    if positiveDigit == 0:
        print("and is 0")
    if (positiveDigit < 6) & (positiveDigit != 0):
        print("and is less than 6 and not 0")


# Case for negative numbers: Converting the last number into a positive
if number < 0:
    negativeDigit = number % -10
    negativeDigit = negativeDigit * -1
    print("Last digit of " + str(number) +  " is " + str(negativeDigit))
    if negativeDigit > 5:
        print("and is greater than 5")
    if negativeDigit == 0:
        print("and is 0")
    if (negativeDigit < 6) & (negativeDigit != 0):
        print("and is less than 6 and not 0")
