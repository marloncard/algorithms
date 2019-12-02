"""
ARRAY:
    : More restrictive than a list in Python
    : Sequence of items accessed or replaced at given index
    : Also allows for length and string representations
    : Typically created with a fixed capacity


"""

class Array:
    """ Represents and array"""
    def __init__(self, capacity, fillValue=None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """Returns array capacity"""
        return len(self._items)

    def __str__(self):
        """Returns string representation of array"""
        return  str(self._items)

    def __iter__(self):
        """Allows for traversal with for loop"""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index"""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index"""
        self._items[index] = newItem


if __name__ ==  '__main__':
    a1 = Array(5)
    print("Length of a1 is: ", len(a1))
    print("String rep of a1: ", a1)

    for i in range(len(a1)):
        a1[i] = i + 1
    print("Replace all elements: ", a1)
    print("Traverse and print all elements: ")
    for e in a1:
        print(e)

    print("Access the last element: ", a1[-1])
