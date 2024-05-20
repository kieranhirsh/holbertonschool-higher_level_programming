#!/usr/bin/python3
''' say_my_name module '''


def print_square(size):
    ''' this function prints a square

    Args:
        size (int): a size of the square
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for ii in range(size):
        for jj in range(size):
            print("#", end="")
        print("")
