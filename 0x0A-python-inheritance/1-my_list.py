#!/usr/bin/python3
""" MyList: inherits stuff from list """


class MyList(list):
    """ MyList, with the stuff inherited from the list """

    def print_sorted(self):
        """ Print the sorted list """
        print(sorted(self))
