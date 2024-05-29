#!/usr/bin/python3
''' module documentation '''


def append_after(filename="", search_string="", new_string=""):
    '''
    this function inserts a line of text to a file, after each line containing
    a specific string

    Arguments:
        filename (str): the file to read/write to
        search_stting (str): hte string after which to add a new string
        new_string (str): the string to add
    '''
    with open(filename, "r") as file:
        text = ""
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as file:
        file.write(text)
