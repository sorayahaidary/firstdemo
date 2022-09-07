import unittest
form circles import circle
from math import pi
class testcircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle(1),pi)
        self.assertaAlmostEqual(circle(0),0)
        self.assertAlmostEqual(circle(2.1),pi*2.1**2)
