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
