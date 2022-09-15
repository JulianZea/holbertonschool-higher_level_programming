#!/usr/bin/python3


def remove_char_at(str, n):
    l = 0
    new = ""
    for i in str:
        if (l != n):
            new += i
        l += 1
    return (new)
