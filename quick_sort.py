"""
Quicksort is considered to be a faster algorithm, comparitively speaking.
It uses the "divide and conquer" strategy to sort a list quickly.

Steps:
    1. Select the item at a list's midpoint (this is called the pivot).
    2. Partition the list so all items less than the pivot are moved to the left
    of the pivot, and the rest to it's right. The final position of the pivot
    is dependent on the particular list (it is rightmost if the largest item
    in the list and leftmost if the smallest).
    3. Reapply the process recursively to the sublists that are created by 
    splitting the list at a pivot. The first sublist consists of all smaller 
    items to the left of the pivot and all larger ones to the right.
    4. The process is complete once it sublists with fewer than two items are
    reached.

The average time complexity of quicksort is O(log n log n) although it can be
O(log n) is the best case and O(n) in the worst.
"""

def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst)-1)
    print(lyst)

def quick_sort_helper(lyst, left, right):
    if left < right:
        pivot_location = partition(lyst, left, right)
        quick_sort_helper(lyst, left, pivot_location-1)
        quick_sort_helper(lyst, pivot_location+1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            lyst[index], lyst[boundary] = lyst[boundary], lyst[index]
            boundary+=1
    # Exchange the pivot item and the boundary item
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]
    return boundary

if __name__ == "__main__":
    quick_sort([9,5,1,8,15,2,6,11])