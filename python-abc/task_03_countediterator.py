#!/usr/bin/python3
''' module documentation '''


class CountedIterator():
    ''' a class '''
    def __init__(self, iterator):
        ''' initialisation method '''
        self.iterator = iter(iterator)
        self.counter = 0

    def __next__(self):
        ''' next method '''
        self.counter += 1
        try:
            return next(self.iterator)
        except StopIteration:
            raise StopIteration

    def get_count(self):
        ''' get_count method '''
        return self.counter
