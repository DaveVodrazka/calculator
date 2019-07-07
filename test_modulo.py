import unittest
from modulo import modulo


class TestModulo(unittest.TestCase):
    def test_values(self):
        # Test modulo for numbers
        self.assertEqual(modulo(5, 3), 2)
        self.assertEqual(modulo(3, 5), 3)
        self.assertEqual(modulo(126, 2), 0)

    def test_types(self):
        # Test modulo for unsupported types
        self.assertRaises(TypeError, modulo, "hello world", 2)
        self.assertRaises(TypeError, modulo, 3 + 2j, 2)
        self.assertRaises(TypeError, modulo, {5}, 0)
        self.assertRaises(TypeError, modulo, 1, [2])
        self.assertRaises(TypeError, modulo, 1.5, 5.5)
