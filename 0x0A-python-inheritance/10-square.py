#!/usr/bin/python3
'''Module for class rectangle'''
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''subclass represents a rectangle.'''
    def __init__(self, size):
        '''Construct'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''area of square.'''
        return self.__size ** 2
