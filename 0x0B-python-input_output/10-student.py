#!/usr/bin/python3
""" Write a class Student that defines a student by: (based on 9-student.py)

 """


class Student:
    """ Contains Student information """
    
    def __init__(self, first_name, last_name, age):
        """ Here's the student info: name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary """

        if not isinstance(attrs=None):
            """ if attrs is not a list of strings """
            new_dictionary = {}
            for attribute in attrs:

                return self.__dict__

        for attribute in attrs:
            if not isinstance(attribute):
                
