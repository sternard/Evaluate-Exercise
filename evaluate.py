import re
from typing import Optional


def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
    if not isinstance(expression, str):
        return None

    try:
        # Allow one optional sign directly attached to ASCII decimal digits.
        integer_pattern = re.compile(r"[+-]?[0-9]+")

        # Both helpers share this cursor so parsing resumes at the correct position
        # after returning from a nested expression.
        position = 0

        def read_operand() -> int:
            """Read a signed integer or evaluate a parenthesised group."""
            nonlocal position

            while position < len(expression) and expression[position].isspace():
                position += 1

            if position < len(expression) and expression[position] == "(":
                position += 1
                value = read_expression()

                if position >= len(expression) or expression[position] != ")":
                    raise ValueError("Missing closing parenthesis")

                position += 1
                return value

            match = integer_pattern.match(expression, position)
            if match is None:
                raise ValueError("Expected an integer or parenthesised expression")

            position = match.end()
            return int(match.group(), 10)

        def read_expression() -> int:
            """Evaluate left to right until a closing parenthesis or end of input."""
            nonlocal position
            result = read_operand()

            while True:
                while position < len(expression) and expression[position].isspace():
                    position += 1

                # Leave ")" for the operand reader that opened this group.
                if position >= len(expression) or expression[position] == ")":
                    return result

                operator = expression[position]
                if operator not in "+-*/":
                    raise ValueError("Expected an arithmetic operator")

                position += 1
                right = read_operand()

                # Apply operations in input order at this nesting level.
                if operator == "+":
                    result += right
                elif operator == "-":
                    result -= right
                elif operator == "*":
                    result *= right
                elif operator == "/":
                    if right == 0:
                        raise ValueError("Division by zero")

                    # Reject fractional results immediately.
                    if result % right != 0:
                        raise ValueError("Non-integral division")

                    result //= right

        result = read_expression()

        # Reject trailing input, including an unmatched closing parenthesis.
        if position != len(expression):
            return None

        return result

    except ValueError:
        # An error at any nesting level invalidates the entire expression.
        return None