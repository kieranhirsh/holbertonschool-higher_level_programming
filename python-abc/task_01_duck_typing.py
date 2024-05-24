#!/usr/bin/python3
''' module documentation '''
from abc import ABC, abstractmethod
import numpy as np


class Shape(ABC):
    ''' this class defines a shape '''
    @abstractmethod
    def area(self):
        """
        Abstract method to define the area of a shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to define the perimeter of a shape
        """
        pass

class Circle(Shape):
    ''' this class defines a Circle, it inherits from Shape '''
    def __init__(self, radius):
        """
        Method to initialize a Circle

        Args:
            radius (float): radius of the Circle
        """
        self.radius = radius

    def area(self):
        """
        Method to define the area of a Circle

        Returns:
            (float): the area of the Circle
        """
        return np.pi * self.radius ** 2

    def perimeter(self):
        """
        Method to define the perimeter of a Circle

        Returns:
            (float): the perimeter of the Circle
        """
        return 2 * np.pi * self.radius

class Rectangle(Shape):
    ''' this class defines a Circle, it inherits from Shape '''
    def __init__(self, width, height):
        """
        Method to initialize a Rectangle

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Method to define the area of a Rectangle

        Returns:
            (float): the area of the Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method to define the perimeter of a Rectangle

        Returns:
            (float): the perimeter of the Rectangle
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Function to print the area and perimeter of a shape
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
