#!/usr/bin/python3
'''Module that looks up a list.'''

def lookup(obj):
    '''Looks up methods and object attributes
    Args:
        obj (object): the object
    Returns:
        list: the list
    '''
    return dir(obj)
