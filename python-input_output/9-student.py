#!/usr/bin/python3
''' module documentation '''


class Student():
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        '''
        initialisation method

        Arguments:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        This module returns the JSON representation of the class

        Returns:
            JSON representation of the object
        '''
        return (self.__dict__)
