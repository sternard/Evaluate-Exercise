from typing import Optional


def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
    try:
        left, right = expression.split("+")
        # Base 10 keeps operands with leading zeros decimal.
        return int(left, 10) + int(right, 10)
    except ValueError:
        return None