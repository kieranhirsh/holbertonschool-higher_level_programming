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
        self.size = size

    @property
    def size(self):
        """
        Getter for the size of the square

        Returns:
            (int): size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square

        Args:
            (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Method to calculate the area of the square

        Returns:
            (int): area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method to print the square
        """
        if self.__size == 0:
            print("")
        else:
            for ii in range(self.__size):
                for jj in range(self.__size):
                    print("#", end="")
                print("")
