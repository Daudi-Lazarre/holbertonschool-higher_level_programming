#!/usr/bin/python3
"""
    Append and write file
"""


def append_write(filename="", text=""):
    """Write a string to a UTF-8 file"""
    with open(filename, 'a', encoding='utf-8') as fd:
        return fd.write(text)
