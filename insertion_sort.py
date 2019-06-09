#!/usr/bin/env python3
"""
Insertion sort starts at the beginning of a list, setting a marker for the 
sorted section. It selects the first unsorted element and swaps other elements
to the right to create the correct position, shifting the unsorted element. It
then advances the marker to the right one element and repeats the process.

It consists of a outer and inner loop, giving it a time complexity of O(n^2)
"""


def insertion_sort(lyst):
    i = 1
    while i < len(lyst):
        item_to_insert = lyst[i]
        j = i - 1
        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = item_to_insert
        i += 1
    return lyst


if __name__ == '__main__':
    print(insertion_sort([5,1,8,3,6,2,]))
