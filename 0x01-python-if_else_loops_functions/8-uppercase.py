#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letterInString = ord(letter)
        if (letterInString >= 97) and (letterInString <= 122):
            letter = chr(letterInString - 32)
        print(letter, end="")
    print("\n", end="")