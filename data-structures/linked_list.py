"""
LINKED LIST:
    : Consists of nodes
    : Each node consists of a value and pointer to another node
    : Starting node is called a header

    Advantages
    : Only allocates memory required for values to be stored
    : Nodes can be located anywhere in memory
    Disadvantages
    : Lookup time is linear

"""
from collections.abc import Sequence


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __len__(self):
        return 1
  

class LinkedList(Sequence):

    def __init__(self):
        self.head = None

    def __len__(self):
        """ Returns the length of the linked list """
        pointer = self.head
        length = 0
        while pointer != None:
            pointer = pointer.next
            length = length + 1
        return length

    def __getitem__(self, index):
        """ Returns the value of the Node at index """
        seek_index = index
        if index < 0:
            seek_index = len(self) + index
        if seek_index < 0:
            raise IndexError("Index out of bounds")
        pointer = self.head
        counter = 0
        while pointer != None:
            if counter == seek_index:
                return pointer.value
            counter = counter + 1
            pointer = pointer.next
        raise IndexError("Index out of bounds")

    def __setitem__(self, index, value):
        seek_index = index
        if index < 0:
            seek_index = len(self) + index
        if seek_index < 0:
            raise IndexError("Index out of bounds")
        pointer = self.head
        counter = 0
        while pointer != None:
            if counter == seek_index:
                pointer.value = value
                return
            counter = counter + 1
            pointer = pointer.next
        raise IndexError("Index out of bounds")
