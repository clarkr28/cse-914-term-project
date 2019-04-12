from unittest import TestCase
from utils import int2hex


class TestInt2hex(TestCase):
    def test_int2hex(self):
        self.assertEqual(int2hex(9, 1), '9')
        self.assertEqual(int2hex(9, 2), '09')
        self.assertEqual(int2hex(9, 3), '009')
        self.assertEqual(int2hex(91, 2), '5b')
        self.assertEqual(int2hex(91, 3), '05b')
        with self.assertRaises(ValueError):
            int2hex(91, 1)
