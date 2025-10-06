def calculate_sum(a: float, b: float) -> float:
    """
    Calculate the sum of two numbers with input validation.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The sum of a and b.

    Raises:
        TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")

    return a + b

def main() -> None:
    try:
        x = 5
        y = 10
        total = calculate_sum(x, y)
        print(f"Sum: {total}")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()