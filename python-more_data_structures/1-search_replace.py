#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of 'search' with 'replace' in a new list.

    Args:
    - my_list: The initial list.
    - search: The element to replace in the list.
    - replace: The new element.

    Returns:
    - A new list with all occurrences of 'search' replaced by 'replace'.
    """
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements of the original list
    for item in my_list:
        # Replace 'search' with 'replace' if found, otherwise keep the original element
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list
