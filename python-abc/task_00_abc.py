#!/usr/bin/python3
''' module documentation '''
from abc import ABC, abstractmethod


class Animal(ABC):
    ''' this class defines an Animal '''
    @abstractmethod
    def sound(self):
        """
        Abstract method define the sound associated with an Animal
        """
        pass

class Dog(Animal):
    ''' this class defines a Dog, it inherits from Animal '''
    def sound(self):
        """
        Method define the sound associated with a dog
        """
        return "Bark"

class Cat(Animal):
    ''' this class defines a Cat, it inherits from Animal '''
    def sound(self):
        """
        Method define the sound associated with a cat
        """
        return "Meow"
