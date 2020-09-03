"""
DYNAMIC ARRAY

    : Similar to a Python list

"""
import ctypes


class DynamicArray:
    """
    Dynamic Array Class
    """
    def __init__(self):
        self.n = 0 # Count of actual elements
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')

        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough
        
        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()


if __name__ == '__main__':
    import sys
    arr = DynamicArray()
    print("Empty array size is: ", sys.getsizeof(arr))
    arr.append(1)
    print("After appending 1, length is: ", len(arr))
    print("Array with 1 element is size: ", sys.getsizeof(arr))
    arr.append(2)
    print("After appending 2, length is: ", len(arr))
    print("Array with 2 elements is size: ", sys.getsizeof(arr))
    print("Accessing index 0 returns: ", arr[0])
    print("Accessing index 1 returns: ", arr[1])

    for i in range(3,1_000_000,10000):
        arr.append(i)
        print("Appending {}, array length is {} and size is {}".format(i, len(arr), sys.getsizeof(arr)))
