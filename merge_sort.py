"""
Merge sort uses a strategy of "divide and conquer" with a recursive algorithm.

Process Summary:
1. Compute a lists middle position and sort it's left and right sublists recursively.
2. Merge the two sorted lists back into a single one.
3. Halt the process once the sublists can no longer be subdivided.

Time Complexity:
Merge sort has an average time complexity of O(n log n)
"""
copy_buffer = []

def merge_sort(lyst):
    return merge_sort_helper(lyst, copy_buffer, 0, len(lyst)-1)
    

def merge_sort_helper(lyst, copy_buffer, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sort_helper(lyst, copy_buffer, low, middle)
        merge_sort_helper(lyst, copy_buffer, middle+1, high)
        merge(lyst, copy_buffer, low, middle, high)


def merge(lyst, copy_buffer, low, middle, high):
    i1 = low
    i2 = middle + 1

    for i in range(low, high+1):
        if i1 > middle:
            copy_buffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copy_buffer[i] = lyst[i]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copy_buffer[i] = lyst[i1]
            i1 += 1
        else:
            copy_buffer[i] = lyst[i2]
            i2 += 1

        for i in range(low, high+1):
            lyst[i] = copy_buffer[i]

    

    
if __name__ == '__main__':
    import random
    merge_sort([9,5,1,8,15,2,6,11])
    #print(merge_sort(random.sample(range(100_000), 2000)))