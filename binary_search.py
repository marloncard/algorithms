"""
A binary search is useful for searching sorted data.

The algorithm starts by comparing the target to the value found in the middle
of the list. If they match, the position is returned. If the value is too low,
the algorithm searches in a higher half of the list at it's new middle position
; if the value is high, it searches in the lower half of the list.

Assumptions:
* Data types are comparable using comparison operators (==, <, >)
* The list is sorted in ascending order.

Time complexity is O(log_2 n)
"""


def binary_search(target, sorted_lyst):
    left = 0
    right = len(sorted_lyst) - 1
    while left <= right:
        midpoint = (left + right) // 2  # O(log n)
        if target == sorted_lyst[midpoint]:
            return midpoint
        elif target < sorted_lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


if __name__ == "__main__":
    print(binary_search(30, [1, 4, 5, 9, 10, 13, 14, 20, 21, 22, 25, 30, 35]))
