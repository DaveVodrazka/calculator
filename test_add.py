import unittest
from add import add


class TestAddition(unittest.TestCase):
    def test_values(self):
        # Test add for numbers
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(.2, 1.7), 1.9)
        self.assertEqual(add(-7.2, -1.7), -8.9)

    def test_types(self):
        # Test add for unsupported types
        self.assertRaises(TypeError, add, "hello world", 2)
        self.assertRaises(TypeError, add, 3+2j, 2)
        self.assertRaises(TypeError, add, {5}, 0)
        self.assertRaises(TypeError, add, 1, [2])
