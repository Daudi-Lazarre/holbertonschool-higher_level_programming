#!/usr/bin/python3
""" BaseGeometry: returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""

class BaseGeometry:
    """ empty class """
    pass

    def area(self):
        """ Raise an exception for area() not implemented """
        raise Exception("area() is not implemented")