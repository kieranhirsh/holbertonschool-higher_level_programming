#!/usr/bin/python3
''' module documentation '''


def write_file(filename="", text=""):
    '''
    This function writes to a file

    Args:
        filename (str): the file to write to
        text (str): the text to write

    Returns:
        (int): the number of characters written
    '''
    with open(filename, "w") as file:
        return file.write(text)
