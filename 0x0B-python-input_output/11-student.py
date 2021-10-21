#!/usr/bin/python3
""" Write a class Student that defines a student by: (based on 9-student.py) """


class Student:
    """ Contains Student information """
    
    def __init__(self, first_name, last_name, age):
        """ Here's the student info: name, age """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary """


        if attrs is not None:
            new_Dictionary = {}
            for i in attrs:
                if i in self.__dict__:
                    new_Dictionary[i] = self.__dict__[i]
            return(new_Dictionary)
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ What is a student? """
        for key, value in json.items():
            self.__dict__[key] = value