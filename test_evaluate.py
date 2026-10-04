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


class SubtractionTests(unittest.TestCase):
    def test_subtract_two_integers(self):
        self.assertEqual(evaluate("3 - 1"), 2)

    def test_returns_integer(self):
        self.assertIs(type(evaluate("1 - 3")), int)

    def test_subtract_to_negative(self):
        self.assertEqual(evaluate("1 - 3"), -2)

    def test_subtract_zero_on_the_left(self):
        self.assertEqual(evaluate("0 - 7"), -7)

    def test_subtract_zero_on_the_right(self):
        self.assertEqual(evaluate("7 - 0"), 7)

    def test_subtract_equal(self):
        self.assertEqual(evaluate("7 - 7"), 0)

    def test_subtract_two_zeros(self):
        self.assertEqual(evaluate("0 - 0"), 0)

    def test_subtract_multi_digit_integers(self):
        self.assertEqual(evaluate("456 - 123"), 333)

    def test_subtract_leading_zeros_as_decimal(self):
        self.assertEqual(evaluate("004 - 008"), -4)


if __name__ == "__main__":
    unittest.main()
