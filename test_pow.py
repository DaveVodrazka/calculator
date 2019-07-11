import unittest
from pow import int_power, int_root, power


class TestIntPower(unittest.TestCase):
    def test_values(self):
        # Test int_pow for numbers
        self.assertAlmostEqual(int_power(2, 3), 8)
        self.assertAlmostEqual(int_power(5, 0), 1)
        self.assertAlmostEqual(int_power(-5, 2), 25)
        self.assertAlmostEqual(int_power(.2, 3), .008)
        self.assertAlmostEqual(int_power(-7.2, 1), -7.2)

    def test_types(self):
        # Test int_pow for unsupported types
        self.assertRaises(TypeError, int_power, "hello world", 2)
        self.assertRaises(TypeError, int_power, 3 + 2j, 2)
        self.assertRaises(TypeError, int_power, {5}, 2)
        self.assertRaises(TypeError, int_power, 1, [2])


class TestIntRoot(unittest.TestCase):
    def test_values(self):
        # Test int_root for numbers
        self.assertAlmostEqual(int_root(4, 2), 2)
        self.assertAlmostEqual(int_root(5, 7), (5 ** (1 / 7)))
        self.assertAlmostEqual(int_root(12, 3), (12 ** (1 / 3)))
        self.assertAlmostEqual(int_root(.345, 4), (.345 ** (1 / 4)))
        self.assertAlmostEqual(int_root(-20, 3), (-20 ** (1 / 3)))

    def test_types(self):
        # Test int_root for unsupported types
        self.assertRaises(TypeError, int_root, "hello world", 2)
        self.assertRaises(TypeError, int_root, 3 + 2j, 2)
        self.assertRaises(TypeError, int_root, {5}, 2)
        self.assertRaises(TypeError, int_root, 1, [2])


class TestMainPower(unittest.TestCase):
    def test_values(self):
        # Test power for numbers
        self.assertAlmostEqual(power(4, 2), 16)
        self.assertAlmostEqual(power(5, -2), 0.04)
        self.assertAlmostEqual(power(7, .5), 2.6457513110646933)
        self.assertAlmostEqual(power(.345, 4), 0.01416695062)
        self.assertAlmostEqual(power(7, -0.81), 0.20676193520878688)

    def test_types(self):
        # Test power for unsupported types
        self.assertRaises(TypeError, power, "hello world", 2)
        self.assertRaises(TypeError, power, 3 + 2j, 2)
        self.assertRaises(TypeError, power, {5}, 2)
        self.assertRaises(TypeError, power, 1, [2])
        self.assertRaises(SyntaxError, power, -4, .25)

