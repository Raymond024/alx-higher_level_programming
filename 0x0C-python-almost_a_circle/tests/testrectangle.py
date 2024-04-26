#!/usr/bin/python3

'''Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
'''

from models.base import Base
from models.rectangle import Rectangle
import io
import sys
import unittest

class TestRectangle_instantiation(unittest.TestCase):
    '''Unittests for testing instantiation of the Rectangle class.'''

    def testrectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def testno_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testone_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testtwo_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def testthree_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def testfour_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def testfive_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def testmore_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def testwidth_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def testheight_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def testx_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def testy_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def testwidth_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def testwidth_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def testheight_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def testheight_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def testx_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def testx_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def testy_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def testy_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_width(unittest.TestCase):
    '''Unittests for testing initialization of Rectangle width attribute.'''

    def testNone_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def teststr_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def testfloat_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def testcomplex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def testdict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def testbool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def testlist_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def testset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def testtuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def testfrozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def testrange_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def testbytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def testbytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def testmemoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def testinf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def testnan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def testnegative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def testzero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def testNone_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def teststr_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def testfloat_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def testcomplex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def testdict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def testlist_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def testset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def testtuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def testfrozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def testrange_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def testbytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def testbytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def testmemoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def testinf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def testnan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def testnegative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def testzero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def testNone_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def teststr_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def testfloat_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def testcomplex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def testdict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def testbool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def testlist_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def testset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def testtuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def testfrozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def testrange_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def testbytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def testbytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def testmemoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def testinf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def testnan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def testnegative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    '''Unittests for testing initialization of Rectangle y attribute.'''

    def testNone_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def teststr_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def testfloat_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def testcomplex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def testdict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def testlist_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def testset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def testtuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def testfrozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def testrange_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def testbytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def testbytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def testmemoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def testinf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def testnan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def testnegative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def testwidth_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def testwidth_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def testwidth_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def testheight_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def testheight_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def testx_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def testarea_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def testarea_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def testarea_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def testarea_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    '''Unittests for testing __str__ and display methods of Rectangle class.'''

    @staticmethod
    def capturestdout(rect, method):
        '''Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        '''

        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def teststr_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def teststr_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def teststr_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def teststr_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def teststr_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def teststr_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def testdisplay_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def testdisplay_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def testdisplay_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def testdisplay_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def testdisplay_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    '''Unittests for testing update args method of the Rectangle class.'''

    # Test args
    def testupdate_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def testupdate_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def testupdate_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def testupdate_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def testupdate_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def testupdate_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def testupdate_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def testupdate_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def testupdate_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def testupdate_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def testupdate_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def testupdate_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def testupdate_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def testupdate_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def testupdate_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def testupdate_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def testupdate_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def testupdate_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def testupdate_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def testupdate_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def testupdate_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def testupdate_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def testupdate_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def testupdate_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def testupdate_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def testupdate_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def testupdate_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def testupdate_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def testupdate_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def testupdate_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def testupdate_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def testupdate_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def testupdate_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def testupdate_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def testupdate_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def testupdate_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def testupdate_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def testupdate_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def testupdate_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def testupdate_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def testupdate_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def testupdate_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def testupdate_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def testupdate_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def testupdate_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def testupdate_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def testupdate_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    '''Unittests for testing to_dictionary method of the Rectangle class.'''

    def testto_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def testto_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def testto_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
