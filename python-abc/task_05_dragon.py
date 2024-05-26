#!/usr/bin/python3
''' module documentation '''


class SwimMixin():
    ''' a mixin class '''
    def swim(self):
        """
        Method
        """
        print("The creature swims!")

class FlyMixin():
    ''' a mixin class '''
    def fly(self):
        """
        Method
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    ''' this class defines a Dragon '''
    def roar(self):
        """
        Method
        """
        print("The dragon roars!")
