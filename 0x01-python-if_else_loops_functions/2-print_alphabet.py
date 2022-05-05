#!/usr/bin/python3

# For each letter in ASCII A to ASCII Z,
# print string literal character letter

for letter in range(97, 123):
    print(f"{chr(letter)}", end="")