#!/usr/bin/python3
""" Square file """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class, import some attrs from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initalize """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size decorator """
        return self.width

    @size.setter
    def size(self, size):
        self.width, self.height = size

    def update(self, *args, **kwargs):
        """ Assigns argument to each attribute. """
        if args:
            attributes = ("id", "width", "height", "x", "y")
            for attribute in range(0, len(args)):
                setattr(self, attributes[attribute], args[attribute])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)


    def __str__(self):
        """ overriding the __str__ method """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height,
        )
