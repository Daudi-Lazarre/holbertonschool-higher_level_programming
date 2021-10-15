#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8) and returns the number of characters added: """


def append_write(filename="", text=""):
    """ must use with statement here """

    with open(filename, mode='a', encoding="UTF-8") as file:
        append_string = file.write(text)
        return(append_string)
