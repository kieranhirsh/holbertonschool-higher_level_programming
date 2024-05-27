#!/usr/bin/python3
''' module documentation '''


def read_file(filename=""):
    '''
    This function prints a file

    Args:
        filename: the file to print
    '''
    with open(filename) as file:
        print(file.read(), end="")
