#!/usr/bin/python3
''' say_my_name module '''


def text_indentation(text):
    ''' this function prints a text with two lines after certain characters

    Args:
        size (int): a size of the square
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline_chars = [".", "?", ":"]

    char = 0
    while char < len(text):
        print(text[char], end="")
        if text[char] in newline_chars:
            print("\n")
            while text[char + 1] == " ":
                char += 1
        char += 1
