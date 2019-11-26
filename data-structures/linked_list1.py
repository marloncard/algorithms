

class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList:

    def __init__(self, root=None):
        self.root_node = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root_node)
        self.root_node = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root_node
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root_node = this_node.get_next()
                self.size -= 1
                return True # Data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # Data not found

    def find(self, data):
        this_node = self.root_node
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    print("Size="+str(ll.get_size()))
    print(ll.remove(4))
    print("Size="+str(ll.get_size()))
    print("Remove 10", ll.remove(10))
    print("Find 23", ll.find(23))
