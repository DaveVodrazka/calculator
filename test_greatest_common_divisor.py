import unittest
from greatest_common_divisor import GCD


class TestGCD(unittest.TestCase):
    def test_values(self):
        # Test GCD for numbers
        self.assertEqual(GCD(5, 3), 1)
        self.assertEqual(GCD(126, 5), 1)
        self.assertEqual(GCD(126, 2), 2)
        self.assertEqual(GCD(84, 126), 42)

    def test_types(self):
        # Test GCD for unsupported types
        self.assertRaises(TypeError, GCD, "hello world", 2)
        self.assertRaises(TypeError, GCD, 3+2j, 2)
        self.assertRaises(TypeError, GCD, {5}, 0)
        self.assertRaises(TypeError, GCD, 1, [2])
        self.assertRaises(TypeError, GCD, 1.5, 5.5)
