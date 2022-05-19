#!/usr/bin/python3
"""
    Base geometry
"""


class BaseGeometry(object):
    """Class def for geometry"""
    def area(self):
        """Returns object area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
