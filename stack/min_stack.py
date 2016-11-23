#!/usr/env/python
from stack import Stack


class MinStack:
    def __init__(self, size=32):
        self.stack = Stack(size)
        self.min_stack = Stack(size)
        self.min_value = 0
        self.size = size
        self.top = -1

    def set_size(self, size):
        self.size = size

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top + 1 == self.size:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empyt")
        else:
            return self.stack[self.top]

    def push(self, obj):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.stack.append(obj)
            self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            self.top -= 1
            return self.stack.pop()

    def show(self):
        print(self.stack)


if __name__ == '__main__':
    s = Stack(5)
    s.push(1)
    s.push(3)
    s.push(9)
    s.push(33)
    s.push(6)
    s.show()
    s.pop()
    s.show()
    s.push(99)
    s.show()
