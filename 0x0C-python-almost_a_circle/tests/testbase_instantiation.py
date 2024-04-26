#!/usr/bin/python3

'''Defines unittests for base.py.'''

from models.rectangle import Rectangle
from models.square import Square
import os
import unittest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def testno_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def testthree_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def testNone_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def testunique_id(self):
        self.assertEqual(12, Base(12).id)

    def testnb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def testid_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def testnb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def teststr_id(self):
        self.assertEqual("hello", Base("hello").id)

    def testfloat_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def testcomplex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def testdict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def testbool_id(self):
        self.assertEqual(True, Base(True).id)

    def testlist_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def testtuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def testset_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def testfrozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def testrange_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def testbytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def testbytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def testmemoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def testinf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def testNaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def testtwo_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
