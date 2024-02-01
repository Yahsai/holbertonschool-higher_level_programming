#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
    - my_list: The list of integers.

    Returns:
    - The sum of all unique integers in the list.
    """
    # Use a set to keep track of unique integers
    unique_numbers = set()

    # Iterate through the elements of the list
    for number in my_list:
        # Add the number to the set if it's not already present
        unique_numbers.add(number)

    # Return the sum of unique integers
    return sum(unique_numbers)

