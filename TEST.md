# 📄 Script Documentation: `test.py`

## 🔍 Overview
This module delivers a small arithmetic toolkit focused on adding two values safely. It now doubles as a command-line program that parses arguments, validates the inputs, and prints the resulting sum or a useful error message.

---

## 📘 Functions

### `_validate_number(value: Real) -> None`
Ensures that a provided value behaves like a real number while protecting against boolean inputs.

- **Parameters**
  - `value` (`Real`): Candidate value to validate.
- **Raises**
  - `TypeError`: If the input is not a real number (or is a boolean).

### `calculate_sum(a: Real, b: Real) -> float`
Validates both operands and returns their sum as a floating-point number.

- **Parameters**
  - `a` (`Real`): First addend.
  - `b` (`Real`): Second addend.
- **Returns**
  - `float`: The sum of `a` and `b`.
- **Raises**
  - `TypeError`: If either argument fails validation.

### `parse_args() -> Tuple[float, float]`
Parses two numeric arguments from the command line using `argparse`.

- **Returns**
  - `Tuple[float, float]`: The two parsed numbers ready for computation.

### `main() -> None`
Orchestrates the CLI: parses inputs, computes the sum, prints the result, and exits with status code `1` on invalid input.

---

## 🚀 Usage

### Run from the command line

```bash
python test.py 3 7
```

Output:

```text
Sum: 10.0
```

If invalid values (e.g., booleans or strings that cannot coerce to floats) are supplied, the script prints an error message and exits with code `1`.

### Use as a library

```python
from test import calculate_sum

calculate_sum(4, 5)      # Returns: 9.0
calculate_sum(2.5, 3.5)  # Returns: 6.0
calculate_sum(True, 2)   # Raises: TypeError
```

---
