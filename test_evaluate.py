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


class MultiplicationTests(unittest.TestCase):
    def test_multiply_two_integers(self):
        self.assertEqual(evaluate("3 * 4"), 12)

    def test_returns_integer(self):
        self.assertIs(type(evaluate("3 * 4")), int)

    def test_multiply_by_one(self):
        self.assertEqual(evaluate("4 * 1"), 4)
        self.assertEqual(evaluate("1 * 7"), 7)

    def test_multiply_by_zero(self):
        self.assertEqual(evaluate("0 * 7"), 0)
        self.assertEqual(evaluate("7 * 0"), 0)

    def test_multiply_two_zeros(self):
        self.assertEqual(evaluate("0 * 0"), 0)

    def test_multiply_multi_digit_integers(self):
        self.assertEqual(evaluate("123 * 456"), 56088)

    def test_multiply_leading_zeros_as_decimal(self):
        self.assertEqual(evaluate("004 * 008"), 32)


class DivisionTests(unittest.TestCase):
    def test_division_two_integers(self):
        self.assertEqual(evaluate("12 / 4"), 3)

    def test_returns_integer(self):
        self.assertIs(type(evaluate("12 / 4")), int)

    def test_division_by_one(self):
        self.assertEqual(evaluate("4 / 1"), 4)

    def test_zero_divided_by_nonzero(self):
        self.assertEqual(evaluate("0 / 7"), 0)

    def test_division_by_zero(self):
        self.assertIsNone(evaluate("7 / 0"))

    def test_division_two_zeros(self):
        self.assertIsNone(evaluate("0 / 0"))

    def test_division_multi_digit_integers(self):
        self.assertEqual(evaluate("408 / 102"), 4)

    def test_division_leading_zeros_as_decimal(self):
        self.assertEqual(evaluate("008 / 004"), 2)

    def test_rejects_non_integral_division(self):
        self.assertIsNone(evaluate("5 / 2"))
        self.assertIsNone(evaluate("1 / 2"))


class OperandTests(unittest.TestCase):
    def test_addition_with_negative_operands(self):
        self.assertEqual(evaluate("-1 + 2"), 1)
        self.assertEqual(evaluate("1 + -2"), -1)
        self.assertEqual(evaluate("-1 + -2"), -3)

    def test_addition_with_positive_signs(self):
        self.assertEqual(evaluate("+1 + 2"), 3)
        self.assertEqual(evaluate("1 + +2"), 3)
        self.assertEqual(evaluate("+1 + +2"), 3)

    def test_subtraction_with_negative_operands(self):
        self.assertEqual(evaluate("-1 - 2"), -3)
        self.assertEqual(evaluate("1 - -2"), 3)
        self.assertEqual(evaluate("-1 - -2"), 1)

    def test_subtraction_with_positive_signs(self):
        self.assertEqual(evaluate("+3 - 2"), 1)
        self.assertEqual(evaluate("3 - +2"), 1)
        self.assertEqual(evaluate("+3 - +2"), 1)

    def test_multiplication_with_negative_operands(self):
        self.assertEqual(evaluate("-3 * 2"), -6)
        self.assertEqual(evaluate("3 * -2"), -6)
        self.assertEqual(evaluate("-3 * -2"), 6)

    def test_multiplication_with_positive_signs(self):
        self.assertEqual(evaluate("+3 * 2"), 6)
        self.assertEqual(evaluate("3 * +2"), 6)
        self.assertEqual(evaluate("+3 * +2"), 6)

    def test_division_with_negative_operands(self):
        self.assertEqual(evaluate("-8 / 2"), -4)
        self.assertEqual(evaluate("8 / -2"), -4)
        self.assertEqual(evaluate("-8 / -2"), 4)

    def test_division_with_positive_signs(self):
        self.assertEqual(evaluate("+8 / 2"), 4)
        self.assertEqual(evaluate("8 / +2"), 4)
        self.assertEqual(evaluate("+8 / +2"), 4)

    def test_accepts_signed_zero_operands(self):
        self.assertEqual(evaluate("-0 + 3"), 3)
        self.assertEqual(evaluate("3 * -0"), 0)
        self.assertEqual(evaluate("0 / -3"), 0)
        self.assertEqual(evaluate("+0 + 3"), 3)

    def test_rejects_non_integral_division_with_signed_operands(self):
        self.assertIsNone(evaluate("-5 / 2"))
        self.assertIsNone(evaluate("5 / -2"))
        self.assertIsNone(evaluate("-5 / -2"))

    def test_rejects_division_by_signed_zero(self):
        self.assertIsNone(evaluate("3 / -0"))
        self.assertIsNone(evaluate("3 / +0"))

    def test_rejects_multiple_signs_on_one_integer(self):
        self.assertIsNone(evaluate("++3 + 2"))
        self.assertIsNone(evaluate("--3 + 2"))
        self.assertIsNone(evaluate("3 + +-2"))
        self.assertIsNone(evaluate("3 + -+2"))
        self.assertIsNone(evaluate("1+++2"))
        self.assertIsNone(evaluate("3 * --2"))


class LeftToRightTests(unittest.TestCase):
    def test_successive_additions(self):
        self.assertEqual(evaluate("1 + 2 + 3"), 6)

    def test_successive_subtractions(self):
        self.assertEqual(evaluate("10 - 3 - 2"), 5)

    def test_successive_multiplications(self):
        self.assertEqual(evaluate("2 * 3 * 4"), 24)

    def test_successive_divisions(self):
        self.assertEqual(evaluate("24 / 4 / 2"), 3)

    def test_multiplication_does_not_take_precedence(self):
        # Ensure traditional BIDMAS results are not respected.
        self.assertEqual(evaluate("1 + 3 * 4"), 16)
        self.assertEqual(evaluate("10 - 2 * 3"), 24)

    def test_division_does_not_take_precedence(self):
        self.assertEqual(evaluate("8 + 4 / 3"), 4)
        self.assertEqual(evaluate("20 - 4 / 4"), 4)

    def test_mixed_operators_in_longer_expression(self):
        self.assertEqual(evaluate("20 + 4 / 6 * 3 - 2"), 10)

    def test_signed_operands_in_successive_operations(self):
        self.assertEqual(evaluate("1+-2*-3"), 3)
        self.assertEqual(evaluate("1--2*3"), 9)
        self.assertEqual(evaluate("-8 / -2 + 3"), 7)
        self.assertEqual(evaluate("+1++2*+3"), 9)

    def test_zero_and_negative_intermediate_results(self):
        self.assertEqual(evaluate("1 + 2 - 3"), 0)
        self.assertEqual(evaluate("1 + 2 - 3 + 4"), 4)
        self.assertEqual(evaluate("1 - 3 * 2 + 5"), 1)

    def test_returns_integer(self):
        self.assertIs(type(evaluate("1 + 3 * 4")), int)

    def test_rejects_non_integral_intermediate_division(self):
        self.assertIsNone(evaluate("5 / 2 * 2"))
        self.assertIsNone(evaluate("5 / 2 * 0"))

    def test_rejects_non_integral_division_after_successful_operations(self):
        self.assertIsNone(evaluate("8 / 2 / 3"))
        self.assertIsNone(evaluate("2 + 3 / 2 * 2"))

    def test_rejects_division_by_zero_in_chain(self):
        self.assertIsNone(evaluate("3 / 0 + 4"))
        self.assertIsNone(evaluate("8 / 2 / 0"))


if __name__ == "__main__":
    unittest.main()
