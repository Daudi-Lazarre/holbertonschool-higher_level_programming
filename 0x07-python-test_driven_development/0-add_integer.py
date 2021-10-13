#!/usr/bin/python3
"""Prints added integer"""


def add_integer(a, b=98):
    """ This function adds numbers"""
    if (a is None or not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
