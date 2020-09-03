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

class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next

    def __repr__(self):
        return "<Node data: {}>".format(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index >= self._size:
            raise IndexError("Index out of range")

        if index == 0:
            return self.head.data

        pointer = self.head
        position = 0

        while position < index:
            pointer = pointer.next_node
            position += 1

        return pointer.data

    def __setitem__(self, index, data):
        if index == 0:
            self.add(data)
            return

        if index > 0:
            new_node = Node(data)

        position = index
        pointer = self.head

        while position > 1:
            pointer = new_node.next_node
            position -= 1
        
        prev_node = pointer
        next_node = pointer.next_node

        prev_node.next_node = new_node
        new_node.next_node = next_node

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        self._size += 1



    def remove(self, data):
        pointer = self.head
        prev_node = None
        found = False
        
        while pointer and not found:
            if pointer.data == data and pointer is self.head:
                found = True
                self.head = pointer.next_node
                self._size -= 1
            elif pointer.data == data:
                found = True
                prev_node.next_node = pointer.next_node
                self._size -= 1
            else:
                prev_node = pointer
                pointer = pointer.next_node

        return pointer

    def find(self, data):
        pointer = self.head
        index = 0

        while pointer:
            if pointer.data == data:
                return index
            else:
                pointer = pointer.next_node
                index += 1
        
        return None


