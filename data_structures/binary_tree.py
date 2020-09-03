import sys


class Node: 
    def __init__(self, data): 
        self.left = None
        self.right = None
        self.data = data

def printInorder(root, counter=0):
    if root: 
        # then print the data of node 
        print(root.data), 
        # print("Level", counter)
        counter = counter + 1
        # First recur on left child 
        printInorder(root.left, counter) 
        
        print("Counter", counter)
        sys.exit()

        # now recur on right child 
        printInorder(root.right, 0)

if __name__ == '__main__':
    root = Node(3)

    root.left = Node(9) 
    root.right = Node(20)

    root.left.left = Node(None) 
    root.left.right = Node(None)
    root.right.left = Node(15)
    root.right.right = Node(7)
    
    root.left.left.left = Node(4)
    # root.left.left.right = Node(6)
    # root.left.right.left = Node(1)
    # root.left.right.right = Node(30)
    root.right.left.left = Node(29)
    # root.right.left.right = Node(17)
    # root.right.right.left = Node(12)
    # root.right.right.right = Node(54)
    

    

    printInorder(root)