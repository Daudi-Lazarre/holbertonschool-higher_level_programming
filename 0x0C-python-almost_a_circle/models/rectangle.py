#!/usr/bin/python3
""" Base class: rectangle """
from models.base import Base


class Base:
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the equivalent of initializing a function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
