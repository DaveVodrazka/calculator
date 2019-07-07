import unittest
from multiply import multiply

class TestMultiplication(unittest.TestCase):
    def test_values(self):
        # Test multiply for numbers
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(.2, 1.7), .34)
        self.assertEqual(multiply(-7.2, -1.7), 12.24)

    def test_types(self):
        # Test multiply for unsupported types
        self.assertRaises(TypeError, multiply, "hello world", 2)
        self.assertRaises(TypeError, multiply, 3+2j, 2)
        self.assertRaises(TypeError, multiply, {5}, 0)
        self.assertRaises(TypeError, multiply, 1, [2])
