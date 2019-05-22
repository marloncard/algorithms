"""
A linear search algorithm that iterates over every record of a list;
it starts at the zero index and check's each item to the right in turn
until a matching value is found.

Assumptions:
Value is present only once or duplicates are ignored (first occurance
will be returned)

Analysis:
1. Worst case the target is at the end of the list or not present at all. The
algorithm visits every item, performing 'n' iterations for list size 'n'.
Worst case complexity is therefore O(n).

2. Best case, the target is at index zero which is a complexity of O(1).

3. To determine average case, add number of iterations required to find the
target at each possible position and divide the sum by n.
(n + n-1 + n-2 + ... + 1)/n or (n+1)/2; average complexity is O(n).
"""


def linear_search(target, a_lyst):
    """Return the position of target or otherwise, 'Not found' """
    position = 0
    while position < len(a_lyst):
        if target == a_lyst[position]:
            return position
        position += 1
    return "Not found"


def linear_search2(target, a_lyst):
    """Return the position of target or otherwise, 'Not found' """
    for i, v in enumerate(a_lyst):
        if target == v:
            return i
    return "Not found"
