#!/usr/bin/python3
""" Rectangle base geometry """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle base class """
    def __init__(self, size):
        """ initial attributes """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ string: width, height """
        return f"[Square] {self.__size}/{self.__size}"
