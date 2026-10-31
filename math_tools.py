"""
MATHEMATICAL TOOLS USING PYTHON

Author: Muhammad Nuhu
Description: A collection of tools for mathematical
calculations and statistical analysis.
"""

import math


def calculate_mean(numbers):
    """Calculate the arithmetic mean."""
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """Calculate the median."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    return sorted_numbers[middle]


def calculate_standard_deviation(numbers):
    """Calculate population standard deviation."""
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def main():
    print("=" * 45)
    print("       MATHEMATICAL TOOLS USING PYTHON")
    print("=" * 45)

    numbers = [10, 20, 30, 40, 50]

    print("\nDataset:", numbers)
    print("Mean:", calculate_mean(numbers))
    print("Median:", calculate_median(numbers))
    print("Standard Deviation:",
          round(calculate_standard_deviation(numbers), 2))


if __name__ == "__main__":
    main()
