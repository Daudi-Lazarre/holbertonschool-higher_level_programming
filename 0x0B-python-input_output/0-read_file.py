#!/usr/bin/python3
""" reads a string to a text file (UTF8) and returns char num. """


def read_file(filename=""):
    """ must use with statement here """

    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
        file.close()
