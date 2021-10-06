#!/usr/bin/python3
""" Define square size """


class Square:
    """verify size with attributes"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")