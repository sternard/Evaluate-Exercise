import re
from typing import Optional


def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
    try:
        # Match two signed integers separated by one arithmetic operator.
        match = re.fullmatch(
            r"\s*([+-]?[0-9]+)\s*([+*/-])\s*([+-]?[0-9]+)\s*",
            expression,
        )

        if match is None:
            return None

        left, operator, right = match.groups()

        if operator == "+":
            # Base 10 keeps operands with leading zeros decimal.
            return int(left, 10) + int(right, 10)
        elif operator == "-":
            return int(left, 10) - int(right, 10)
        elif operator == "*":
            return int(left, 10) * int(right, 10)
        elif operator == "/":
            left = int(left, 10)
            right = int(right, 10)

            if right == 0:
                return None

            # Reject division that would produce a fractional result.
            if left % right != 0:
                return None

            return left // right
        else:
            return None
    except ValueError:
        return None