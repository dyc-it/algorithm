#!/usr/evn python

from BinaryTreeNode import BinaryTreeNode


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
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        else:
            return None


if __name__ == "__main__":
    # random_list = random.sample(range(1, 10), 9)
    # print random_list
    random_list = [0, 8, 1, 6, 2, 4, 3, 5, 9, 7]
    tree = BinarySearchTreeNode(None, None, None, None)
    for i in random_list:
        tree.add(i, "data-"+str(i))

    print 'in order'
    BinarySearchTreeNode.in_order(tree)

    search_key = 8
    print '\nsearch key: ' + str(search_key)
    searched_node = tree.search(search_key)
    if searched_node:
        print 'searched value: ' + searched_node.value





