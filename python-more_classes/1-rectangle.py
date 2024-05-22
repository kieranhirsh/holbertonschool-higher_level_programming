#!/usr/bin/python3
''' module documentation. is empty for now '''


class Rectangle:
    ''' this class will define a rectangle, it does nothing for now though '''
    def __init__(self, width=0, height=0):
        """
        Method to initialize a rectangle

        Args:
            width (int): width of the rectangle
            height (int): width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle

        Returns:
            (int): width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle

        Args:
            value (int): width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle

        Returns:
            (int): height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle

        Args:
            value (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
