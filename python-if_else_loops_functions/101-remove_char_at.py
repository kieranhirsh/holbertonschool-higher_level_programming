#!/usr/bin/python3

def remove_char_at(str, n):
    if n >= 0:
        return str[:n] + str[n + 1:]
    elif n < 0:
        return str
    else:
        return "n is neither positive nor negative"
