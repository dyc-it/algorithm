# -*- coding:utf-8 -*-
class BinaryHeap(object):
    """
    实现一个小根堆。
    小根堆的性质:任何结点都小于它的任意一个子结点。
    """
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.list = [0] * (capacity + 1)
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def insert(self, key):
        """
        percolate up,上浮
        在最后插入新的结点new,如果new破坏了堆序性,则将new的父结点放到new的位置;
        再看new在新的位置是否破坏了堆序性,如果破坏了,继续将new的父结点放到new新的位置。
        直到满足了堆序性。
        复杂度分析:每插入一个结点复杂度为O(logn)
        :param key:
        :return:
        """
        if self.is_full():
            raise Exception("binary heap is full")

        # index represent the insert location just after the size location.
        self.size += 1
        index = self.size
        while self.list[index / 2] > key:
            self.list[index] = self.list[index / 2]
            index /= 2
        self.list[index] = key

    def delete_min(self):
        """
        下沉 percolate down
        当删除一个最小结点时(就是根结点),根结点上会有空位。
        1.如果堆中最后一个元素last可以放到根结点,那么delete_min就完成了。
        2.如果堆中最后一个元素放到根结点后,破坏了堆序性,那么根结点和它小一点的孩子互换。
        3.重复步骤2,直到满足堆序性
        :return:
        """

        if self.is_empty():
            return None

        min_key = self.list[1]
        last_key = self.list[self.size]
        self.size -= 1

        index = 1  # represent the root node
        while index * 2 <= self.size:
            # get the child node
            child_index = index * 2
            # get the litter child(in case some node only have one child).
            if child_index != self.size \
                    and self.list[child_index + 1] < self.list[child_index]:
                child_index += 1
            # 如果最后一个元素大于根结点的子结点中较小值,用较小的子结点替换根结点;
            # 否则, 满足堆序性,算法结束。
            if last_key > self.list[child_index]:
                self.list[index] = self.list[child_index]
            else:
                break
            index = child_index

        self.list[index] = last_key
        return min_key

    def build_from_list_nlogn(self, input_list):
        """
        复杂度分析:每插入一个结点复杂度为O(logn),所以插入n个节点的复杂度是O(nlogn)
        :param input_list:
        :return:
        """
        for key in input_list:
            self.insert(key)

    def build_from_list_logn(self, input_list):
        pass


