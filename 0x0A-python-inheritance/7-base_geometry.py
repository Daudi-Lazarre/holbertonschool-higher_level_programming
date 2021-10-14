#!/usr/bin/python3
""" BaseGeometry again """


class BaseGeometry:
    """ Class """

    def area(self):
        """ This is a public class """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
