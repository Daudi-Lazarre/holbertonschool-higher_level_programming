#!/usr/bin/python3
""" Reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ must use with statement here """

    with open(filename, encoding="UTF-8") as file:
        print(filename)
        read_the_line = file.read()
        print(read_the_line, end="")
