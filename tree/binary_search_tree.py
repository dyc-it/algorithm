#!/usr/evn python
from binary_tree import BinaryTreeNode


class BinarySearchTreeNode(BinaryTreeNode):
    def add(self, key, value):
        if self.key is None:
            self.key = key
            self.value = value
            pass
        if key < self.key:
            if self.left is not None:
                self.left.add(key, value)
            else:
                node = BinarySearchTreeNode(key, value, None, None)
                self.left = node
        if key > self.key:
            if self.right is not None:
                self.right.add(key, value)
            else:
                node = BinarySearchTreeNode(key, value, None, None)
                self.right = node

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
        if self.left is None:
            return self
        else:
            return self.left.min()

    def max(self):
        if self.right is None:
            return self
        else:
            return self.right.max()

    def delete(self, key):
        if not self:
            return None
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

