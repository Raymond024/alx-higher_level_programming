#!/usr/bin/python3

'''Defines unittests for models/rectangle.py.'''

from models.base import Base
from models.rectangle import Rectangle
import io
import sys
import unittest

class TestRectangle_area(unittest.TestCase):
    '''Unittests for testing the area method of the Rectangle class.'''

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
    def capture_stdout(rect, method):
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

if __name__ == "__main__":
    unittest.main()
