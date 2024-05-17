#!/usr/bin/python3
''' add_integer module '''


def add_integer(a, b=98):
    ''' this function adds two integers together 
    
    Args:
        a (int/float): an integer
        b (int/float): another integer

    Returns:
        (int): the sum fo the two integers
    '''
    if not isinstance(a, int) and not isinstance(a, float) or a % 0 != 0:
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float) or b % 0 != 0:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
