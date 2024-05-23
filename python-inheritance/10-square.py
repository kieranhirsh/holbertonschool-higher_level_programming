#!/usr/bin/python3
""" a module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle class
    """
    def __init__(self, size):
        """
        This function initialises a square

        Arguments:
            size (int): the size of the square
            height (int): the width of the rectange
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Method to define the print() behaviour of this class
        """
        return str(Rectangle(self.__size, self.__size))

    def area(self):
        """
        This function calculates the area of a rectangle

        Returns:
            (int): the area of a rectangle
        """
        return self.__size * self.__size
