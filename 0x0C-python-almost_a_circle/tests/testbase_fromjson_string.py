#!/usr/bin/python3

'''Defines unittests for base.py'''
from models.square import Square
from models.rectangle import Rectangle
import os
import unittest
from models.base import Base

class TestBase_fromjson_string(unittest.TestCase):
    '''Unittests for testing from_json_string method of Base class.'''

    def testfrom_jsonstring_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def testfrom_jsonstring_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def testfrom_jsonstring_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def testfrom_jsonstring_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def testfrom_jsonstring_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def testfrom_jsonstring_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def testfrom_jsonstring_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def testfrom_jsonstring_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testfrom_jsonstring_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

if __name__ == "__main__":
    unittest.main()
