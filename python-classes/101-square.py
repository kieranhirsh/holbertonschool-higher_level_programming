#!/usr/bin/python3
''' module documentation. is empty for now '''


class Square:
    ''' this class defines a square

    Args:
        size (int): the square's size
        position (size 2 tuple of ints): position of the square

    Attributes (int):
        size: the square's size'''
    def __init__(self, size=0, position=(0, 0)):
        """
        Method to initialize a square

        Args:
            size (int): size of the square
            position (size 2 tuple of ints): position of the square
        """
        self.size = size
        self.position = position

    def __str__(self):
        """
        Method to define the print() behaviour of this class
        this is just the my_print method modified to have a
        return value since print() demands a string be returned
        """
        if self.__size == 0:
            return ""
        else:
            for y in range(self.__position[1]):
                print("")
            for ii in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for jj in range(self.__size):
                    print("#", end="")
                if ii != self.__size - 1:
                    print("")
        return ""

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

    @property
    def position(self):
        """
        Getter for the position of the square

        Returns:
            (tuple): position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square

        Args:
            (size 2 tuple of ints): position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(ii, int) for ii in value) or
                any(ii < 0 for ii in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Method to calculate the area of the square

        Returns:
            (size 2 tuple of ints): area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method to print the square
        """
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print("")
            for ii in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for jj in range(self.__size):
                    print("#", end="")
                print("")
