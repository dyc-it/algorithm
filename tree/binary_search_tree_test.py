import unittest
import random

from binary_search_tree import BinarySearchTreeNode


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        size = 10
        self.random_list = random.sample(range(0, size), size)
        self.random_list = [5, 3, 6, 1, 2, 4, 9, 0, 7, 8]
        print "random list generated: " + str(self.random_list)

        self.tree = BinarySearchTreeNode(None, None, None, None)
        for key in self.random_list:
            self.tree.add(key, "data-"+str(key))

        self.existed_key = random.sample(self.random_list, 1)[0]
        self.existed_key = 8
        print "existed_key: " + str(self.existed_key)
        self.non_existed_key = size + 1

    def tearDown(self):
        pass

    def test_min(self):
        min_value = min(self.random_list)
        self.assertEqual(min_value, (self.tree.min()).key)

    def test_max(self):
        max_value = max(self.random_list)
        self.assertEqual(max_value, (self.tree.max()).key)

    def test_search(self):
        existed_node = self.tree.search(self.existed_key)
        self.assertEqual(self.existed_key, existed_node.key)

        non_existed_node = self.tree.search(self.non_existed_key)
        self.assertEqual(non_existed_node, None)

    def test_delete(self):
        self.tree.delete(self.existed_key)
        print '\npre order'
        self.tree.pre_order()
        print '\nin order'
        self.tree.in_order()
