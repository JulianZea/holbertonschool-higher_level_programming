#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j in range (len(i)):
            print("{:d}".format(i[j]), end='')
            if j is not len(i):
                print(" ", end='')
        print()
