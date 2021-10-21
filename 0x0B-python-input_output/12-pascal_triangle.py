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
    two_Dimensional_List = []
    if n > 0:
        temp = []
        for line in range(1, n + 1):
            num = 1
            for i in range(1, line + 1):
                temp.append(num)
                # This is the meat of the math right here...
                num = int(num * (line - i) / i)
            two_Dimensional_List.append(temp)
            temp = []
    return two_Dimensional_List



