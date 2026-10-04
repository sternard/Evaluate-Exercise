import unittest

from evaluate import evaluate


class AdditionTests(unittest.TestCase):
    def test_adds_two_integers(self):
        self.assertEqual(evaluate("1 + 3"), 4)

    def test_returns_integer(self):
        self.assertIs(type(evaluate("1 + 3")), int)

    def test_adds_zero_on_the_left(self):
        self.assertEqual(evaluate("0 + 7"), 7)

    def test_adds_zero_on_the_right(self):
        self.assertEqual(evaluate("7 + 0"), 7)

    def test_adds_two_zeros(self):
        self.assertEqual(evaluate("0 + 0"), 0)

    def test_adds_multi_digit_integers(self):
        self.assertEqual(evaluate("123 + 456"), 579)

    def test_interprets_leading_zeros_as_decimal(self):
        self.assertEqual(evaluate("004 + 008"), 12)


if __name__ == "__main__":
    unittest.main()
