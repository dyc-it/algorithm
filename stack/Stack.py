#!/usr/env python
class Stack:
    def __init__(self):
        self.stack = []
        self.top_index = -1

    def is_empty(self):
        if self.top_index == -1:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.top_index]

    def push(self, obj):
        self.stack.append(obj)
        self.top_index += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            self.top_index -= 1
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
