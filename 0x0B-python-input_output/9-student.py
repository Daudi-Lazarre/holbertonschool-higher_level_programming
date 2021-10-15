#!/usr/bin/python3
""" Write a class Student that defines a student by: """


class Student:
    """ Contains Student information """
    
    def __init__(self, first_name, last_name, age):
        """ Here's the student info: name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary """
        self.__dict__

        return self.__dict__
