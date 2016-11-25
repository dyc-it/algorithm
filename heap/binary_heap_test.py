import unittest
import random

from binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        size = 8
        self.random_list = random.sample(range(0, size), size)
        print "random list generated: " + str(self.random_list)

        self.heap = BinaryHeap(size)
        for key in self.random_list:
            if not self.heap.is_full():
                self.heap.insert(key)

    def tearDown(self):
        pass

    def test_delete_min(self):
        order_list = sorted(self.random_list)
        index = 0
        while not self.heap.is_empty():
            min_value = self.heap.delete_min()
            print min_value
            self.assertEqual(min_value, order_list[index])
            index += 1


