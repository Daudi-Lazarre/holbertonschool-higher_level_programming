#!/usr/bin/python3
"""
inherits_from: returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """ the object is or isn't a class: Returns True and False """

    return isinstance(obj, a_class) and type(obj) != a_class
