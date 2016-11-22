#!/usr/evn python
from queue.Queue import Queue


class BinaryTreeNode:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def pre_order(node):
        if node is not None:
            print node.key,
            if node.left is not None:
                node.pre_order(node.left)
            if node.right is not None:
                node.pre_order(node.right)

    @staticmethod
    def in_order(node):
        if node is not None:
            if node.left is not None:
                node.in_order(node.left)
            print node.key,
            if node.right is not None:
                node.in_order(node.right)

    @staticmethod
    def post_order(node):
        if node is not None:
            if node.left is not None:
                node.post_order(node.left)
            if node.right is not None:
                node.post_order(node.right)
            print node.key,

    @staticmethod
    def level_order(node):
        q = Queue()
        while node is not None:
            print node.key,
            if node.left is not None:
                q.add(node.left)
            if node.right is not None:
                q.add(node.right)
            node = None if q.is_empty() else q.delete()

if __name__ == '__main__':
    node_2 = BinaryTreeNode(2, None, None, None)
    node_3 = BinaryTreeNode(3, None, None, None)
    tree = BinaryTreeNode(1, None, node_2, node_3)

    print 'pre order:'
    BinaryTreeNode.pre_order(tree)
    print '\nin order'
    BinaryTreeNode.in_order(tree)
    print '\npost order'
    BinaryTreeNode.post_order(tree)
    print '\nlevel order'
    BinaryTreeNode.level_order(tree)

