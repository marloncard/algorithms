from unittest import TestCase

from data_structures.linked_list import Node, LinkedList


class TestNode(TestCase):

    def test_make_nodes(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        n1.next_node = n2
        n2.next_node = n3

        self.assertEqual(n2.next_node.data, n3.data,
            "n2's next_node.data should return n3's data value")

class TestLinkedList(TestCase):

        def setUp(self):

            self.ll = LinkedList()

        def tearDown(self):
            pass

        def test_add_len(self):
            self.ll.add("one")
            self.ll.add("two")
            self.ll.add("three")

            self.assertEqual(self.ll.head.data, "three",
                "Last node added is 3")
            self.assertEqual(len(self.ll), 3,
                "length of linked list should be 3")

        def test_get(self):
            self.ll.add("one")
            self.ll.add("two")
            self.ll.add("three")

            self.assertEqual(self.ll[1], "two",
                "getter of 1st index should return two")
            self.assertEqual(self.ll[0], "three",
                "getter of 0th index should return three")

        def test_set(self):
            self.ll[0] = "apple"
            self.assertEqual(self.ll[0], "apple",
                "0th index should contain apple")

            self.ll.add("banana")
            self.ll.add("pear")
            self.ll[1] = "mango"
            self.assertEqual(self.ll[1], "mango",
                "1st index should contain mango")

        def test_remove(self):
            self.ll.add("apple")
            self.ll.add("banana")
            self.ll.add("pear")
            self.assertEqual(len(self.ll), 3,
                "linked list should initially have length of 3")

            self.ll.remove("banana")
            self.assertEqual(self.ll[1], "apple",
                "1st index of linked list should be apple")
            self.assertEqual(self.ll[0], "pear",
                "0th index of linked list should be pear")
            self.assertEqual(len(self.ll), 2,
                "new length of linked list should be 2")

        def test_find(self):
            self.ll.add("apple")
            self.ll.add("banana")
            self.ll.add("pear")
            
            self.assertEqual(self.ll.find("banana"), 1,
                "banana should be located at 1st index")
            self.assertEqual(self.ll.find("apple"), 2,
                "apple should be located at 2nd index")


