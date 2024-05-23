#!/usr/bin/python3
""" a module """


class MyInt(int):
    ''' this class is MyInt '''
    def __init__(self, size):
        """
        This function initialises an int

        Arguments:
            size (int): the size of the square
        """
        self.__size = size

    def __eq__(self, another_int):
        """
        Method to determine if this int == another int, but swapped

        Args:
            another_int (int): another int

        Return:
            (bool): True, if this int != another int
                    False, if not
        """
        return not self.__size == another_int

    def __ne__(self, another_int):
        """
        Method to determine if this int != another int, but swapped

        Args:
            another_int (int): another int

        Return:
            (bool): True, if this int != another int
                    False, if not
        """
        return not self.__size != another_int
