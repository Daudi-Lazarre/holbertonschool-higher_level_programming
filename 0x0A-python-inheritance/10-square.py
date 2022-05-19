#!/usr/bin/python3
"""
    Square python file
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Refer to rectangle"""
    def __init__(self, size):
        """New square is made"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
