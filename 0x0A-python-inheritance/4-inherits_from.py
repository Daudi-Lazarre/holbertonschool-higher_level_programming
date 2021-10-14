#!/usr/bin/python3
""" inherits_from: """


def inherits_from(obj, a_class):
    """ the object is or isn't a class: Returns True and False """

    return isinstance(obj, a_class) and type(obj) != a_class
