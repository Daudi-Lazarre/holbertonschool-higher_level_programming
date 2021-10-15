#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns char num. """


def write_file(filename="", text=""):
    """ must use with statement here """

    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
