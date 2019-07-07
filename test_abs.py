import unittest
from abs import abs


class TestAbs(unittest.TestCase):
    def test_values(self):
        # Test abs for numbers
        self.assertEqual(abs(5), 5)
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(-3), 3)
        self.assertEqual(abs(-0.123), 0.123)

    def test_types(self):
        # Test abs for unsupported types
        self.assertRaises(TypeError, abs, "hello world")
        self.assertRaises(TypeError, abs, 3+2j)
        self.assertRaises(TypeError, abs, {5})
        self.assertRaises(TypeError, abs, [2])
