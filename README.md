## Overview

Implements a Python function with the following interface:

```
def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
```

### Valid tokens

| Token         | Specification |
| --- | --- |
| `<number>`    | Only signed decimal integers (0-9). |
| `( )`         | Nested expressions should be evaluated first. |
| `+, -, *, /`  | Basic operators: addition, subtraction, multiplication and division. |

### Examples

| Input | Return value |
| --- | --- |
| `1 + 3` | `4` |
| `(1 + 3) * 2 ` | `8` |
| `(4 / 2) + 6` | `8` |
| `4 + (12 / (1 * 2))` | `10` |
| `(1 + (12 * 2)` | `None` |

## Usage

To run the test suite, execute `python3 -m unittest -v` from the project directory. 

## Requirements

- Expressions should be parsed left to right instead of using standard order of operations.
- Evaluate parenthesised expressions first, and then use their results in the surrounding expression. Support nested parentheses and apply the same left to right ordering within each group.
- Ignore whitespace between tokens - [see Whitespace under Assumptions for detailed interpretation](#whitespace).
- Return an integer for a successful evaluation, or `None` if an error occurs.
- Do not use any external libraries or built-in expression functions e.g. `eval()`.

## Assumptions

### Whitespace

- Spaces, tabs and line breaks are accepted as whitespace.
- Ignored whitespace cannot convert two tokens into a single token. `1 2` is invalid and returns `None`, rather than being interpreted as `12`.
- A sign is part of an integer token and must be immediately followed by its digits, so `-2` is valid but `- 2` is invalid.

### Division

- Every division must produce a signed decimal integer, otherwise the evaluation will return `None` immediately.
- This rule also applies to intermediate calculations and expressions inside parentheses. `(5 / 2) * 2` returns `None`, even though allowing a fractional intermediate result would make the final result valid.
- Dividing by zero will return `None`.

| Input | Return value |
| --- | --- |
| `8 / 2` | `4` |
| `5 / 2` | `None` |
| `-8 / 2` | `-4` |
| `-5 / 2` | `None` |
| `0 / 3` | `0` |
| `3 / 0` | `None` |
| `3 / (3 - 3)` | `None` |

### Numbers and signs

- An integer may have one optional leading `+` or `-`. Explicit positive signs are accepted, so `+4` returns `4`.
- Signed integers may appear wherever an operand is expected. `1+-2` returns `-1`, `1--2` returns `3`, and `1++2` returns `3`. `1+++2` returns `None`.
- Multiple signs on a single integer, such as `--2`, are invalid. Signs applied directly to parenthesised expressions, such as `-(2+3)`, are also invalid.
- Leading zeros are accepted and interpreted as decimal digits. For example, `004` returns `4`.

### Invalid expressions

- Parentheses may enclose a single integer, so `(7)` returns `7`. Empty parentheses are invalid.
- Every pair of operands requires an explicit operator. Implied multiplication, such as `2(3+4)` or `(2)(3)`, is invalid.
- Empty or whitespace-only input, missing operands or operators, unmatched parentheses, unsupported characters, and unsupported numeric formats return `None`.
- The complete input must form one valid expression. Unconsumed or invalid trailing content causes the evaluation to return `None`.
- An error anywhere in an expression causes the entire evaluation to return `None`.
- Inputs are strings. Non-string inputs return `None`.