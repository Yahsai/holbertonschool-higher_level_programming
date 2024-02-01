#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
    - a_dictionary: The input dictionary.

    Returns:
    - The key with the biggest integer value, or None if no score is found.
    """
    # Check if the dictionary is not None and not empty
    if a_dictionary:
        # Find the key with the maximum value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None
