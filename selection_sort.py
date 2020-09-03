#!/usr/bin/env python3
"""
The 'Selection Sort' algorithm searches the entire list for the position of the
smallest item. If that position does not equal the first position, then those 
two items are swapped. The algorithm then returns to the second position and 
repeats this process, swapping the smallest item with the item at the second 
position if necessary.

Has a best, average and worst case time complexity of O(n^2) because of the 
double while statements and because every item is iterated over even if list is
sorted.
"""


def selection_sort(lyst):
    iter_counter = 0 # No purpose other than to prove sorted vs unsorted lists
    i = 0
    # Do n - 1 searches
    while i < len(lyst) - 1: # O(n)
        min_index = i
        j = i + 1

        iter_counter += 1 #

        # Start a search
        while j < len(lyst): # O(n)
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1

            iter_counter += 1

        # Exchange if necessary
        if min_index != i:
            lyst[min_index], lyst[i] = lyst[i], lyst[min_index] # O(1)
        i += 1

    return (lyst, iter_counter)


if __name__ == '__main__':
    print(selection_sort([5,10,9,1,3,2,8,7]))
    print(selection_sort([1,2,3,5,7,8,9,10]))