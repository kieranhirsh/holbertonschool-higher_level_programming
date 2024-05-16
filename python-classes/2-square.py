#!/usr/bin/python3
''' module documentation. is empty for now '''


class Square:
    ''' this class defines a square '''
    def __init__(self, size=0):
        """
        Initialize a square

        Args:
            size (int): size of the  square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
