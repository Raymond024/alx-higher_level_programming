#!/usr/bin/python3
'''Module for class rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    '''A subclass of class rectangle'''
    def __init__(self, width, height):
        '''Construct'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
