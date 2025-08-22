import numpy as np

# Collection of different number sets
number_sets = {
    "Set 1": [44, 12, 93, 8, 29, 56, 74, 1],
    "Set 2": [1, 3, 5, 7, 9, 11, 13, 15],
    "Set 3": [2, 4, 4, 4, 4, 5, 6, 10],
    "Set 4": [10, 20, 30, 40, 50, 60, 70, 8000],
    "Set 5": list(range(1, 1001)),
    "Set 6": [2 ** x for x in range(15)],
    "Set 7": sorted(np.random.randint(1, 1000, size=100).tolist()),
    "Set 8": [5] * 50 + [100000],
    "Set 9": list(np.random.randint(1, 1000, size=50)),
    "Set 10": sorted([1] * 40 + [2, 3, 4, 5, 6])
}

# The specific number find in each set
target_numbers = {
    "Set 1": 56,
    "Set 2": 11,
    "Set 3": 4,
    "Set 4": 8000,
    "Set 5": 999,
    "Set 6": 1024,
    "Set 7": 875,
    "Set 8": 100000,
    "Set 9": 750,
    "Set 10": 3
}


def simple_search(mixed_numbers, target):
    """Look through numbers one by one (good for unsorted data)"""
    checks = 0
    for position, number in enumerate(mixed_numbers):
        checks += 1
        if number == target:
            return position, checks
    return -1, checks


def smart_ordered_search(ordered_numbers, target):
    """Search in order but stop early if we pass the target"""
    checks = 0
    for position, number in enumerate(ordered_numbers):
        checks += 1
        if number == target:
            return position, checks
        elif number > target:
            break
    return -1, checks


def binary_divide_search(ordered_numbers, target):
    """Repeatedly divide the search area in half (very efficient for sorted data)"""
    checks = 0
    left, right = 0, len(ordered_numbers) - 1

    while left <= right:
        checks += 1
        middle = (left + right) // 2
        if ordered_numbers[middle] == target:
            return middle, checks
        elif ordered_numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, checks


def smart_guess_search(uniform_numbers, target):
    """Make educated guesses about position (best for evenly spaced numbers)"""
    checks = 0
    left, right = 0, len(uniform_numbers) - 1

    while left <= right and uniform_numbers[left] != uniform_numbers[right]:
        checks += 1
        guess = left + ((target - uniform_numbers[left]) * (right - left) //
                        (uniform_numbers[right] - uniform_numbers[left]))

        if guess < 0 or guess >= len(uniform_numbers):
            break

        if uniform_numbers[guess] == target:
            return guess, checks
        elif uniform_numbers[guess] < target:
            left = guess + 1
        else:
            right = guess - 1
    return -1, checks


def examine_number_set(numbers):
    """Understand the nature of our number set"""
    is_ordered = numbers == sorted(numbers)
    evenly_spaced = False
    has_extreme_value = False

    if is_ordered and len(numbers) > 1:
        gap = numbers[1] - numbers[0]
        evenly_spaced = all(numbers[i] - numbers[i - 1] == gap for i in range(1, len(numbers)))

        # Calculate statistical boundaries
        quarter_point = np.percentile(numbers, 25)
        three_quarter_point = np.percentile(numbers, 75)
        spread = three_quarter_point - quarter_point
        lower_limit = quarter_point - (1.5 * spread)
        upper_limit = three_quarter_point + (1.5 * spread)
        has_extreme_value = any(x < lower_limit or x > upper_limit for x in numbers)

    return is_ordered, evenly_spaced, has_extreme_value


if __name__ == "__main__":
    print("Number Search Results")
    print("=" * 30)

    for set_name in sorted(number_sets.keys()):
        numbers = number_sets[set_name]
        target = target_numbers[set_name]

        # Understand this number set's characteristics
        ordered, uniform, has_outlier = examine_number_set(numbers)

        # Choose the best search method
        if set_name == "Set 1":
            method = "Simple Search"
        elif set_name == "Set 2" and uniform:
            method = "Smart Guess Search"
        elif set_name == "Set 3" and ordered:
            method = "Binary Divide"
        elif set_name == "Set 4" and has_outlier:
            method = "Binary Divide"
        elif set_name == "Set 5" and uniform:
            method = "Smart Guess Search"
        elif set_name == "Set 6" and ordered:
            method = "Binary Divide"
        elif set_name == "Set 7" and ordered:
            method = "Binary Divide"
        elif set_name == "Set 8" and ordered:
            method = "Binary Divide"
        elif set_name == "Set 9":
            method = "Simple Search"
        elif set_name == "Set 10" and ordered:
            method = "Binary Divide"
        else:
            method = "Binary Divide"

        # Now perform the actual search
        if method == "Simple Search":
            position, _ = simple_search(numbers, target)
        elif method == "Smart Ordered Search":
            position, _ = smart_ordered_search(numbers, target)
        elif method == "Binary Divide":
            position, _ = binary_divide_search(numbers, target)
        elif method == "Smart Guess Search":
            position, _ = smart_guess_search(numbers, target)

        was_found = position != -1
        print(f"{set_name} | {method} | {'Found' if was_found else 'Not found'}")