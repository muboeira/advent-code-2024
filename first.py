from collections import Counter


def calculate_distance(filename="input.txt"):
    """
    Calculates the total distance between corresponding elements from two lists
    read from a file.

    Args:
        filename (str): Path to the input file containing two columns of numbers

    Returns:
        int: Total distance between corresponding elements
    """
    try:
        with open(filename, "r") as file:
            # Using list comprehension and tuple unpacking
            first_list, second_list = zip(
                *([int(num) for num in line.split()] for line in file)
            )

            # Calculate total distance using sum() and map()
            distance = sum(
                abs(a - b) for a, b in zip(sorted(first_list), sorted(second_list))
            )

            return distance

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except ValueError:
        print("Error: File contains invalid number format")
        return None


def calculate_proximity(filename="input.txt"):
    """
    Calculates the total proximity between corresponding elements from two lists
    read from a file by multiplying the frequency of matching elements with the
    element value.

    Args:
        filename (str): Path to the input file containing two columns of numbers

    Returns:
        int: Total proximity score, or None if an error occurs

    Example:
        If first_list has [1,1,2] and second_list has [1,2,2],
        then for 1: count=1 (from second_list) * 1 = 1
        and for 2: count=2 (from second_list) * 2 = 4
        Total proximity = 5
    """
    try:
        with open(filename, "r") as file:
            first_list, second_list = zip(
                *([int(num) for num in line.split()] for line in file)
            )

            # Count frequencies of elements in both lists
            first_counter = Counter(first_list)
            second_counter = Counter(second_list)

            # Calculate proximity using generator expression
            proximity = sum(
                second_counter[key] * key
                for key in first_counter
                if key in second_counter
            )

            return proximity

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except ValueError:
        print("Error: File contains invalid number format")
        return None


if __name__ == "__main__":
    result = calculate_distance()
    if result is not None:
        print(f"Total distance: {result}")
    result_proximity = calculate_proximity()
    if result_proximity is not None:
        print(f"Total proximity: {result_proximity}")
