import unittest
from area import *
from perimeter import *


class MyTestCase(unittest.TestCase):
    """
    A class to test area and perimeter modules
    """
    delta_value = 0.001

    def test_cir(self):
        self.assertAlmostEqual(cir(2), 12.566, delta=self.delta_value)  # add assertion here

    def test_rec(self):
        self.assertAlmostEqual(rec(2, 3.5), 7, delta=self.delta_value)

    def test_squ(self):
        self.assertAlmostEqual(squ(2.6), 6.76, delta=self.delta_value)

    def test_tri(self):
        self.assertAlmostEqual(tri(3, 6.2), 9.3, delta=self.delta_value)

    def test_circle(self):
        self.assertAlmostEqual(circle(4.5), 28.274, delta=self.delta_value)  # add assertion here

    def test_rectangle(self):
        self.assertAlmostEqual(rectangle(2, 3.5), 11, delta=self.delta_value)

    def test_square(self):
        self.assertAlmostEqual(square(2.6), 10.4, delta=self.delta_value)

    def test_triangle(self):
        self.assertAlmostEqual(triangle(3, 6.2, 3.2), 12.4, delta=self.delta_value)


if __name__ == '__main__':
    unittest.main()
