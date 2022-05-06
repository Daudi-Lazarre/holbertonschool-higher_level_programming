#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letterStr = ord(i)
        if (letterStr >= 97) and (letterStr <= 122):
            letter = chr(letterStr - 32)
        print(letter, end="")
    print("\n", end="")
