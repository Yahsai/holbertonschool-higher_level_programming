#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
    - a_dictionary: The input dictionary.
    - key: The key (always a string) to replace or add.
    - value: The value (any type) to set for the key.

    Returns:
    - The updated dictionary.
    """
    # Update the value if the key exists, otherwise add a new key-value pair
    a_dictionary[key] = value
    return a_dictionary
