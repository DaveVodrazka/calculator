import unittest
from fraction import get_fraction


class TestGetFraction(unittest.TestCase):
    def test_values(self):
        # Test get_fraction for numbers
        self.assertEqual(get_fraction(1.5), (3, 2))
        self.assertEqual(get_fraction(4.2), (21, 5))
        self.assertEqual(get_fraction(.12), (3, 25))
        self.assertEqual(get_fraction(-5.6312), (-7039, 1250))

    def test_types(self):
        # Test get_fraction for unsupported types
        self.assertRaises(TypeError, get_fraction, "hello world")
        self.assertRaises(TypeError, get_fraction, 3+2j)
        self.assertRaises(TypeError, get_fraction, {5})
        self.assertRaises(TypeError, get_fraction, [2])
