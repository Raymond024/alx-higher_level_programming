#!/usr/bin/python3
'''Module for class rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    '''subclass represents a rectangle.'''
    def __init__(self, width, height):
        '''Construct'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''returns area of rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''method for string representation'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
