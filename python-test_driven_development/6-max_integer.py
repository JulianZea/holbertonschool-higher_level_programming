#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    result = list[0]

    if list:
        if len(list) == 0:
            return None
            i = 1
            while i < len(list):
                if list[i] > result:
                    result = list[i]
                i += 1
    if list[-1] == result:
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] != list[-1]:
                result = list[i]
                break
            i += 1

    return result
