#!/usr/bin/python3
""" a module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        This function initialises a rectangle

        Arguments:
            width (int): the width of the rectange
            height (int): the width of the rectange
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Method to define the print() behaviour of this class
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        This function calculates the area of a rectangle

        Returns:
            (int): the area of a rectangle
        """
        return self.__width * self.__height
