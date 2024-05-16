#!/usr/bin/python3
''' module documentation. is empty for now '''


class Square:
    ''' this class defines a square

    Args:
        size (int): the square's size

    Attributes (int):
        size: the square's size'''
    def __init__(self, size=0):
        """
        Method to initialize a square

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
