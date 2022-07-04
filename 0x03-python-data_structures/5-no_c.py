#!/usr/bin/python3

def no_c(my_string):
    """Removes all c characters from string"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
