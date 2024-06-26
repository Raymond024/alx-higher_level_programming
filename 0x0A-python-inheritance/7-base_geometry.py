#!/usr/bin/python3
'''Module for BaseGeometry'''

class BaseGeometry:
    '''A BaseGeometry'''
    def area(self):
        '''Method to calculate the area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method to validate value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
