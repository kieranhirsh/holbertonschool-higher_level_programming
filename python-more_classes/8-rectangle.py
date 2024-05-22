#!/usr/bin/python3
''' module documentation. is empty for now '''


class Rectangle:
    ''' this class will define a rectangle, it does nothing for now though '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Method to initialize a rectangle

        Args:
            width (int): width of the rectangle
            height (int): width of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """
        Method to define the print() behaviour of this class
        """
        rect = ""

        if self.width == 0 or self.height == 0:
            return ""

        for ii in range(self.height):
            for jj in range(self.width):
                rect += str(self.print_symbol)
            rect += "\n"

        return rect[:-1]

    def __repr__(self):
        """
        Method that returns the command required to initialise a copy of this
        rectangle

        Returns:
            (str): the desired command as a string
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor method for the rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """
        Method to calculate hte area of the rectangle

        Returns:
            (int): area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method to calculate the perimeter of the rectangle

        Returns:
            (int): perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * self.width + 2 * self.height

    def bigger_or_equal(rect_1, rect_2):
        """
        Method to calculate the bigger of two rectangles, based on area

        Args:
            rect_1 (Rectangle): a Rectangle
            rect_2 (Rectangle): a Rectangle

        Returns:
            (Rectangle): the larger of the two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
