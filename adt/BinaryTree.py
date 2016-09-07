#!/usr/evn python
from Queue import Queue


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        
    def __init__(self, data, left, right):
        self.root = Node(data, left, right)
    
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    
    def pre_order(self, r):
        if r.root is not None:
            print r.root.data,
            if r.root.left is not None:
                self.pre_order(r.root.left)
            if r.root.right is not None:
                self.pre_order(r.root.right)

    def in_order(self, r):
        if r.root is not None:
            if r.root.left is not None:
                self.in_order(r.root.left)
            print r.root.data,
            if r.root.right is not None:
                self.in_order(r.root.right)

    def post_order(self, r):
        if r.root is not None:
            if r.root.left is not None:
                self.post_order(r.root.left)
            if r.root.right is not None:
                self.post_order(r.root.right)
            print r.root.data,

    def level_order(self, r):
        q = Queue()
        while r is not None:
            print(r.root.data), 
            if r.root.left is not None:
                q.add(r.root.left)  
            if r.root.right is not None:
                q.add(r.root.right)  
            if q.is_empty():
                r = None
            else:  
                r = q.delete() 

            
if __name__ == "__main__":
    g = BinaryTree('G', None, None)
    h = BinaryTree('H', None, None)
    e = BinaryTree('E', g, h)
    d = BinaryTree('D', None, None)
    b = BinaryTree('B', d, e)
    f = BinaryTree('F', None, None)
    c = BinaryTree('C', None, f)
    a = BinaryTree('A', b, c)
    
    print("preOrder")
    a.pre_order(a)
    print("\ninOrder")
    a.in_order(a)
    print("\npostOrder")
    a.post_order(a)
    print("\nlevelOrder")
    a.level_order(a)
