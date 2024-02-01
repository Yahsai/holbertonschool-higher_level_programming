#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
    - a_dictionary: The input dictionary.
    - key: The key (always a string) to delete.

    Returns:
    - The updated dictionary.
    """
    # Delete the key if it exists
    a_dictionary.pop(key, None)
    return a_dictionary
