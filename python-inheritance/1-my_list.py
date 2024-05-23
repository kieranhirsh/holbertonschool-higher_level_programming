#!/usr/bin/python3
""" a module """


class MyList(list):
    ''' this class is MyList '''
    def print_sorted(self):
        """
        Method to print a list in ascending order
        """
        print_list = self.copy()
        print_list.sort()
        print(print_list)
