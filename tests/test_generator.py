import unittest

from src.generator import generate_password
from src.strength import check_strength


class TestGenerator(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(generate_password(20)), 20)

    def test_too_short(self):
        with self.assertRaises(ValueError):
            generate_password(2)

    def test_has_digit_when_enabled(self):
        for _ in range(200):
            self.assertTrue(any(c.isdigit() for c in generate_password(8)))


class TestStrength(unittest.TestCase):
    def test_weak(self):
        self.assertEqual(check_strength("abc"), "weak")

    def test_strong(self):
        self.assertEqual(check_strength("Abcdef123456!"), "strong")


if __name__ == "__main__":
    unittest.main()