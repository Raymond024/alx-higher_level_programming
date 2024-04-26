#!/usr/bin/python3

"""Defines unittests for base.py."""

from models.rectangle import Rectangle
from models.square import Square
import os
import unittest
from models.base import Base

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def testto_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def testto_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def testto_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def testto_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def testto_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def testto_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def testto_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def testto_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def testto_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def testto_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
