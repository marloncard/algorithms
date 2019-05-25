"""
The 'Selection Sort' algorithm searches the entire list for the position of the smallest item.
If that position does not equal the first position, then those two items are swapped. The algorithm
then returns to the second position and repeats this process, swapping the smallest item with the 
item at the second position if necessary.

Has a time complexity of O(n^2) because of the double while statements
"""


def selection_sort(lyst):
    i = 0
    # Do n - 1 searches
    while i < len(lyst) - 1:
        min_index = i
        j = i + 1
        # Start a search
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        # Exchange if necessary
        if min_index != i:
            lyst[min_index], lyst[i] = lyst[i], lyst[min_index]
        i += 1
    return lyst


if __name__ == '__main__':
    print(selection_sort([5,10,9,1,3,2,8,7]))