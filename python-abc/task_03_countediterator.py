#!/usr/bin/python3
''' module documentation '''


class CountedIterator():
    ''' a class '''
    def __init__(self, some_iterable):
        ''' initialisation method '''
        self.iterator = iter(some_iterable)
        self.counter = 0

    def __iter__(self):
        ''' iter method '''
        return self

    def __next__(self):
        ''' next method '''
        try:
            item = next(self.iterator)
        except StopIteration:
            raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        ''' get_count method '''
        return self.counter
