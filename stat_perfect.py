from typing import List, Dict, Union
import math


def calculate_statistics(data: List[float]) -> Dict[str, Union[float, None, int]]:
    """
    Calculate descriptive statistics for a given list of numeric data.
    
    Args:
        data (List[float]): A list of numeric values.
    
    Returns:
        Dict[str, Union[float, None, int]]: A dictionary containing mean, median, variance,
        standard deviation, and count. Returns None for mean/median/variance/std_dev if the list is empty.
    """
    if not data:
        return {
            'mean': None,
            'median': None,
            'variance': None,
            'std_dev': None,
            'count': 0
        }

    count = len(data)
    total = sum(data)
    mean = total / count

    sorted_data = sorted(data)
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]

    if count > 1:
        variance = sum((x - mean) ** 2 for x in data) / (count - 1)
    else:
        variance = 0.0

    std_dev = math.sqrt(variance)

    return {
        'mean': mean,
        'median': median,
        'variance': variance,
        'std_dev': std_dev,
        'count': count
    }


def find_outliers(data: List[float], threshold: float = 2.0) -> List[float]:
    """
    Identify outliers in the data using Z-score method.

    Args:
        data (List[float]): A list of numeric values.
        threshold (float): Z-score threshold above which a value is considered an outlier.

    Returns:
        List[float]: A list of outlier values.
    """
    if not data or len(data) < 2:
        return []

    stats = calculate_statistics(data)
    mean = stats['mean']
    std_dev = stats['std_dev']

    if std_dev == 0 or std_dev is None:
        return []

    return [
        value for value in data
        if abs((value - mean) / std_dev) > threshold
    ]


def moving_average(data: List[float], window_size: int) -> List[float]:
    """
    Compute the moving average of the given data using a specified window size.

    Args:
        data (List[float]): A list of numeric values.
        window_size (int): The number of elements to include in each average.

    Returns:
        List[float]: A list of moving averages.

    Raises:
        ValueError: If the window size is not positive or larger than the data length.
    """
    if not data:
        return []

    if window_size <= 0:
        raise ValueError("Window size must be a positive integer.")
    if window_size > len(data):
        raise ValueError(f"Window size ({window_size}) cannot be larger than data length ({len(data)}).")

    return [
        sum(data[i:i + window_size]) / window_size
        for i in range(len(data) - window_size + 1)
    ]


# -------------------------------
# ✅ Test Code with Edge Cases
# -------------------------------

def test_functions():
    empty_data = []
    single_data = [5]
    normal_data = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9]

    print("=== Testing: Empty Data ===")
    print(f"Stats: {calculate_statistics(empty_data)}")

    print("\n=== Testing: Single Data Point ===")
    print(f"Stats: {calculate_statistics(single_data)}")

    print("\n=== Testing: Outlier Detection ===")
    print(f"Outliers in {normal_data}: {find_outliers(normal_data)}")

    print("\n=== Testing: Moving Average (valid window size) ===")
    try:
        ma = moving_average(normal_data, 3)
        print(f"Moving Average (window=3): {ma}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\n=== Testing: Moving Average (invalid window size) ===")
    try:
        ma = moving_average(normal_data, 15)
        print(f"Moving Average: {ma}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_functions()
