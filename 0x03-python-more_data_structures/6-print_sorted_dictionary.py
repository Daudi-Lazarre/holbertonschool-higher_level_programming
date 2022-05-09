#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedKeys = list(sorted((a_dictionary.keys())))
    for i in sortedKeys:
        print("{}: {}".format(i, a_dictionary[i]))
