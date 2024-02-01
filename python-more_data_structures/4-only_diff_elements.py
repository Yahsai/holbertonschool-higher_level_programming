#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
    - set_1: The first set.
    - set_2: The second set.

    Returns:
    - A set containing elements present in only one of the input sets.
    """
    # Use the symmetric difference operation to find elements present in only one set
    only_diff_set = set_1 ^ set_2
    return only_diff_set
