#!/usr/bin/python3
"""
Contains MyInt
"""
class MyInt(int):
    """opposite type of integer, perfect for the opposite"""
    def __new__(cls, *args, **kwargs):
        """new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was not equal is now equal"""
        return int(self) != other

    def __ne__(self, other):
        """what was equal is now not equal"""
        return int(self) == other
