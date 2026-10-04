import re
from typing import Optional


def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
    try:
        # Allow one optional sign directly attached to ASCII decimal digits.
        integer_pattern = r"[+-]?[0-9]+"

        # Validate the entire sequence of signed integers and operators before
        # finditer extracts operations, so invalid input cannot be skipped.
        match = re.fullmatch(
            rf"\s*({integer_pattern})((?:\s*[+*/-]\s*{integer_pattern})+)\s*",
            expression,
        )

        if match is None:
            return None

        first, remaining = match.groups()
        result = int(first, 10)

        # Apply each operation to the running result in input order.
        for operation in re.finditer(
            rf"([+*/-])\s*({integer_pattern})",
            remaining,
        ):
            operator, right = operation.groups()
            right = int(right, 10)

            if operator == "+":
                result += right
            elif operator == "-":
                result -= right
            elif operator == "*":
                result *= right
            elif operator == "/":
                if right == 0:
                    return None

                # Reject fractional results immediately.
                if result % right != 0:
                    return None

                result //= right

        return result
    except ValueError:
        return None