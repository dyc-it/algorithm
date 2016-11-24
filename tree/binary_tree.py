#!/usr/evn python
from queue.Queue import Queue
from stack.stack import Stack


class BinaryTreeNode:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def is_empty(self):
        # if self.key is None, we consider the tree is empty
        return self.key is None

    def pre_order(self):
        if self is not None:
            print self.key,
            if self.left is not None:
                self.left.pre_order()
            if self.right is not None:
                self.right.pre_order()

    def in_order(self):
        if self is not None:
            if self.left is not None:
                self.left.in_order()
            print self.key,
            if self.right is not None:
                self.right.in_order()

    def post_order(self):
        if self is not None:
            if self.left is not None:
                self.left.post_order()
            if self.right is not None:
                self.right.post_order()
            print self.key,

    def level_order(self):
        level_order_list = []
        q = Queue()
        while self is not None:
            level_order_list.append(self)
            if self.left is not None:
                q.add(self.left)
            if self.right is not None:
                q.add(self.right)
            self = None if q.is_empty() else q.delete()
        return level_order_list

    def pre_order_not_recursion(self):
        pre_order_list = []
        node = self
        s = Stack()
        while node or not s.is_empty():
            while node:
                pre_order_list.append(node)
                s.push(node)
                node = node.left
            if not s.is_empty():
                node = (s.pop()).right
        return pre_order_list

    def in_order_not_recursion(self):
        in_order_list = []
        node = self
        s = Stack()
        while node or not s.is_empty():
            while node:
                s.push(node)
                node = node.left
            if not s.is_empty():
                node = s.pop()
                in_order_list.append(node)
                node = node.right
        return in_order_list

    def post_order_recursion(self):
        post_order_list = []
        node = self
        pre_node = None
        current_node = None
        s = Stack()
        s.push(node)

        while not s.is_empty():
            current_node = s.top()
            if (not current_node.left and not current_node.right ) or \
                    (pre_node and (pre_node.key == current_node.left.key or pre_node.key == current_node.right.key)):
                post_order_list.append(current_node)
                s.pop()
                pre_node = current_node
            else:
                if current_node.right:
                    s.push(current_node.right)
                if current_node.left:
                    s.push(current_node.left)
        return post_order_list


if __name__ == '__main__':
    node_2 = BinaryTreeNode(2, None, None, None)
    node_3 = BinaryTreeNode(3, None, None, None)
    tree = BinaryTreeNode(1, None, node_2, node_3)
    print 'pre order'
    tree.pre_order()

    print '\npre order not recursion'
    pre_order_list = tree.pre_order_not_recursion()
    for node in pre_order_list:
        print node.key,

    print '\nin order'
    tree.in_order()

    print '\nin order not recursion'
    in_order_list = tree.in_order_not_recursion()
    for node in in_order_list:
        print node.key,

    print '\npost order'
    tree.post_order()

    print '\npost order not recursion'
    post_order_list = tree.post_order_recursion()
    for node in post_order_list:
        print node.key,

    print '\nlevel order'
    level_order_list = tree.level_order()
    for node in level_order_list:
        print node.key,




