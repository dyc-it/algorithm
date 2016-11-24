# -*- coding:utf-8 -*-
# !/usr/evn python
from binary_tree import BinaryTreeNode


class BinarySearchTreeNode(BinaryTreeNode):
    """
    Binary Search Tree Node
    """
    def add(self, key, value):
        if self.is_empty():  # if tree is empty, use the first node as root
            self.key = key
            self.value = value
        else:
            if key < self.key:  # put the little node on the left
                if self.left:
                    self.left.add(key, value)
                else:
                    self.left = BinarySearchTreeNode(key, value, None, None)
            if key > self.key:  # put the great node on the right
                if self.right:
                    self.right.add(key, value)
                else:
                    self.right = BinarySearchTreeNode(key, value, None, None)

    def search(self, key):
        if key == self.key:
            return self
        elif self.left and key < self.key:
            return self.left.search(key)
        elif self.right and key > self.key:
            return self.right.search(key)
        else:
            return None

    def min(self):
        # if self has no left child, then it's the minimum node
        return self.left.min() if self.left else self

    def max(self):
        # if self has no right child, then it's the maximum node
        return self.right.max() if self.right else self

    def delete(self, key):
        if key > self.key:
            self.right = self.right.delete(key)
        elif key < self.key:
            self.left = self.left.delete(key)
        else:
            if self.left and self.right:
                min_at_right = self.right.min()
                self.key = min_at_right.key
                self.value = min_at_right.value
                self.right = self.right.delete(min_at_right.key)
            else:
                self = self.left if self.left else self.right
        return self

