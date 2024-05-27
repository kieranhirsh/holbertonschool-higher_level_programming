#!/usr/bin/python3
''' module documentation '''


def append_write(filename="", text=""):
    '''
    This function appends to a file

    Args:
        filename (str): the file to append to
        text (str): the text to append

    Returns:
        (int): the number of characters appended
    '''
    with open(filename, "a") as file:
        return file.write(text)
