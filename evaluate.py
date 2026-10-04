from typing import Optional


def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
    try:
        if "+" in expression:
            left, right = expression.split("+")
            # Base 10 keeps operands with leading zeros decimal.
            return int(left, 10) + int(right, 10)
        elif "-" in expression:
            left, right = expression.split("-")
            return int(left, 10) - int(right, 10)
        elif "*" in expression:
            left, right = expression.split("*")
            return int(left, 10) * int(right, 10)
        elif "/" in expression:
            left, right = expression.split("/")
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