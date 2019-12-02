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

    def __delitem__(self, index):
        """ Deletes the node at index """
        seek_index = index
        if index < 0:
            # Account for negative idices 4 + (-1) = index of 3
            seek_index = len(self) + index
        # If we still have a negative index raise an IndexError
        if seek_index < 0:
            raise IndexError("Index out of bounds")
        pointer = self.head
        newll = LinkedList()
        newll.head = Node(None)
        counter = 0
        while pointer != None:
            if counter == seek_index:
                while pointer.next != None:
                    pointer.value = pointer.next.value
                    pointer = pointer.next
                return
            counter += 1
            newll.head = pointer.head
            pointer = pointer.next


    def insert(self, index, value):
        seek_index = index
        if index < 0:
            seek_index = len(self) + index
        if seek_index < 0:
            raise IndexError("Index out of bounds")
        if seek_index == 0:
            new_node = Node(value) # Create new node with value
            new_node.next = self.head # Assign new node.next value of self.head
            self.head = new_node # Assign self.head new_node's value
        else:
            pointer = self.head
            counter = 0
            while pointer != None:
                if counter == seek_index - 1:
                    new_node = Node(value)
                    new_node.next = pointer.next
                    pointer.next = new_node
                    return
                counter = counter + 1
                pointer = pointer.next
            raise IndexError("Index out of bounds")


if __name__ == '__main__':
    ml = LinkedList()
    ml.head = Node(1)
    ml.head.next = Node(2)
    ml.head.next.next = Node(3)
    ml.head.next.next.next = Node(4)
    # assert len(ml) == 3, "length = the number of Nodes"

    # ml.insert(0,4)
    # print((ml[0], ml[1], ml[2], ml[3]))
    # assert ml[0] == 4, """[] retrieves correct item
    #     & insert places at correct index"""

    # ml[1] = "pie"
    # assert ml[1] == "pie", "setitem works"
    print((ml[0], ml[1], ml[2], ml[3]))
    print(len(ml))
    del(ml[1])
    print((ml[0], ml[1], ml[2], ml[3]))
    print(len(ml))