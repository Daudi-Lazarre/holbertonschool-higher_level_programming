#!/usr/bin/python3
""" Module: Pascal's Triangle """


def pascal_triangle(n):
    """ A set of lists that contain integers
    and those lists are in a list...
    which will ultimately form a 2D list.
    
    empty_list = no numbers
    two_dimensional_list = the main list
    one_dimensional_lists = the multiple lists within the bigger list 
    """
    two_dimensional_list = []
    if n <= 0:
        """ print numbers in every spot"""
        empty_list = []
        return empty_list
    
    for line in range(1, n + 1):
        line.append(1)
        # I lost track of what I'm doing. Time to take a break.
        for line 

