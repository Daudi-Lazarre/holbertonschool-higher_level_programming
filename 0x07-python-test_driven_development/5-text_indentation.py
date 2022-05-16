#!/usr/bin/python3
"""
Print two lines after characters
"""


def text_indentation(text):
    """
    Print indentation, type error, must be string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    newtext = text.replace('?', '?\n\n')
    newtext = newtext.replace('.', '.\n\n')
    newtext = newtext.replace(':', ':\n\n')

    print("\n".join([item.strip() for item in newtext.split("\n")]), end="")
