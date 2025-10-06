# 📄 Script Documentation: `sum_calculator.py`

## 🔍 Overview
This script provides a simple utility to calculate the sum of two numeric values with built-in input validation and error handling. It includes a main function to usage.

---

## 

### `calculate_sum(a: float, b: float) -> float`
Calculates the sum of two numbers after validating that both inputs are either integers or floats.

**Parameters:**
- `a` (float or int): The first number.

**Returns:**
- `float`: The sum of `a` and `b`.

**Raises:**
- `TypeError`: 

---

### `main() -> None`
Demonstrates the use of `calculate_sum` by adding two predefined numbers (`x = 5`, `y = 10`).  and prints any `TypeError` exceptions raised during execution.

---

## 🚀 Usage

Run the script directly:

```bash
python sum_calculator.py
```

Output: Sum: 15

calculate_sum(3, 7)     # Returns: 10
calculate_sum(4.5, 2.5) # Returns: 7.0
calculate_sum("3", 5)   # Raises: TypeError

---