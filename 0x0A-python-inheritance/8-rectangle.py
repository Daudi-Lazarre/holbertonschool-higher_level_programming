#!/usr/bin/python3
""" Rectangle base geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle base class """

    def __init__(self, width, height):
        """ instantiatian: inherits from baseGeom """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

