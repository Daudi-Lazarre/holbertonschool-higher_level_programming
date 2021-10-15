#!/usr/bin/python3
""" returns the dictionary description... serialization """


def class_to_json(obj):
    """ Dictionary description: Class to JSON """

    return(obj.__dict__)
