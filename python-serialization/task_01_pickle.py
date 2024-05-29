#!/usr/bin/python3
''' module documentation '''
import pickle


class CustomObject:
    '''
    a custom class

    Attributes (int):
        name: a str
        age: an int
        is_student: a bool
    '''
    def __init__(self, name, age, is_student):
        '''
        initialisation method
        
        Arguemnts:
            name: a str
            age: an int
            is_student: a bool
        '''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''
        method to print a CustomObject's attributes
        '''
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        '''
        method to serialise and save CustomObject to a file

        Arguments:
            filename (str): the file to save to
        '''
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        '''
        This method creates a CustomObject from a file

        Args:
            filename (str): the file to read

        Returns:
            filename converted into a CustomObject
        '''
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
