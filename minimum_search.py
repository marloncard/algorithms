"""
This algorithm searches for the minumum value in a list. The zero
index is assigned by default and if a smaller value is found it is assigned
as minimum. The search ends once the final index item is evaluated and then the
index location containing the minimum value is returned.
"""


def min_search(a_lyst):
    # Set default minimum index as first (index zero) position
    min_index = 0
    current_index = 1
    while current_index < len(a_lyst):
        if a_lyst[current_index] < a_lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index


def min_search2(a_lyst):
    # Set default minimum index as first (index zero) position
    min_index = 0
    for i, v in enumerate(a_lyst):
        if v < a_lyst[min_index]:
            min_index = i
    return min_index
