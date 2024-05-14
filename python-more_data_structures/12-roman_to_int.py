#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    roman_int = roman_dict[roman_string[0]]
    ii = 1

    while ii < len(roman_string):
        # this logic is terrible because the code style doesn't like lines over
        # 80 caracters and won't let me break up an if statement into 2 lines
        # of code.
        # it's much more intuitive to look forward to decide whether to add or
        # subract a number than it is to look backwards and retroactively
        # subtract twice the previous number.
        if roman_dict[roman_string[ii]] > roman_dict[roman_string[ii - 1]]:
            roman_int -= 2 * roman_dict[roman_string[ii - 1]]

        roman_int += roman_dict[roman_string[ii]]

        ii += 1

    return roman_int
