#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
    - a_dictionary: The input dictionary.

    Prints:
    - The dictionary's key-value pairs sorted by alphabetic order of keys.
    """
    # Iterate through the sorted keys and print key-value pairs
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
