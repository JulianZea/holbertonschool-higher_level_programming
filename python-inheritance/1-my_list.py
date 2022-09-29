#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """
        Print list sorted
        """
        new_list = self[:]
        print(sorted(new_list))
