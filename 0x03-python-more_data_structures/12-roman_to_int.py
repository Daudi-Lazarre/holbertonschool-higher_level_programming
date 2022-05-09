#!/usr/bin/python3
def roman_to_int(roman_string):
    romanNumeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    output = 0
    index = 1

    if not roman_string or type(roman_string) != str:
        return 0
    if len(roman_string) == 1:
        return (romanNumeral[roman_string[0]])
    for index in range(1, len(roman_string)):
        if romanNumeral[roman_string[index - 1]] < romanNumeral[roman_string[index]]:
            output += (romanNumeral[roman_string[index - 1]] * -1)
        else:
            output += romanNumeral[roman_string[index - 1]]
    
    output += romanNumeral[roman_string[index]]
    return output
