#!/usr/bin/python3
""" Write a text file (UTF8) and prints it to stdout """


def write_file(filename="", text=""):
    """ must use with statement here """

    with open(filename, mode="w", encoding="UTF-8") as file:
        write_the_line = file.write(text)
    return(write_the_line)
