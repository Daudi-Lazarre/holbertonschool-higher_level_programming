#!/usr/bin/python3
""" Text Indentation """


def text_indentation(text):
    """ Function that indents text """

    if type(text) is not str:
        raise TypeError("text must be a string")

    newtext = text.replace('?', '?\n\n')
    newtext = newtext.replace('.', '.\n\n')
    newtext = newtext.replace(':', ':\n\n')
    print("\n".join([item.strip() for item in newtext.split("\n")]), end="")