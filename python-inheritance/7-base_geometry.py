#!/usr/bin/python3
""" a module """


class BaseGeometry():
    """
    BaseGeometry class
    """
    def area(self):
        """
        This function raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value

        Arguments:
            name (str): the name of the value
            value (int): the value of the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
