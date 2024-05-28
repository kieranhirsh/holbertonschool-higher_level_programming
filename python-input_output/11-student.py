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

    def to_json(self, attrs=None):
        '''
        This module returns the JSON representation of the class

        Arguments:
            attrs (list of str): the atrributes to return (return all if None)

        Returns:
            JSON representation of the object
        '''
        if attrs is None:
            return self.__dict__

        temp = self.__dict__
        Jason = dict()

        for key in temp:
            if key in attrs:
                Jason[key] = temp[key]

        return Jason

    def reload_from_json(self, json):
        '''
        This module that replaces all attributes of a Student instance

        Arguments:
            json (dict): the new attributes
        '''
        for key in json:
            self.__dict__[key] = json[key]
