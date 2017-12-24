import unittest

import fibonacci as fb


class Test(unittest.TestCase):

    def test_zero(self):
        self.assertListEqual(fb.first_n(0), [])

    def test_first_one(self):
        self.assertListEqual(fb.first_n(1), [1])

    def test_first_two(self):
        self.assertListEqual(fb.first_n(2), [1, 1])

    def test_first_three(self):
        self.assertListEqual(fb.first_n(3), [1, 1, 2])

    def test_first_four(self):
        self.assertListEqual(fb.first_n(4), [1, 1, 2, 3])

    def test_first_five(self):
        self.assertListEqual(fb.first_n(5), [1, 1, 2, 3, 5])

    def test_first_ten(self):
        self.assertListEqual(fb.first_n(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

