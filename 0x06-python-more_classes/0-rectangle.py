#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    def __init__(self, width=0, height=0):
        """ * Launching rectangle into existence * """
        self.height = height
        self.width = width
    
    @property
    def height(self):
        """ Remember: Decorators allow for attributes to be modified """
        """ Set the height of the rectangle """
        return self.__height
    
    @height.setter
    def height(self, num):
        """ Set the height """
        if type(num) is not int:
            raise TypeError("height must be an integer")
        if num < 0:
            raise ValueError("height must be >= 0")
        self.__height = num

    @property
    def width(self):
        """ Set the width """
        return self.__width

    @width.setter
    def width(self, num):
        """ Set the width """
        if type(num) is not int:
            raise TypeError("width must be an integer")
            if num < 0:
                raise ValueError("width must be >= 0")
            self.__width = num
