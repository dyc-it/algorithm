#!/usr/env python
class Queue:  
    def __init__(self, size=16):
        self.queue = []  
        self.size = size  
        self.front = 0  
        self.rear = 0

    def is_empty(self):
        return self.rear == 0  

    def is_full(self):
        if (self.front - self.rear + 1) == self.size:
            return True  
        else:  
            return False  

    def first(self):
        if self.is_empty():
            raise Exception("QueueIsEmpty")  
        else:  
            return self.queue[self.front]  

    def last(self):
        if self.is_empty():
            raise Exception("QueueIsEmpty")  
        else:  
            return self.queue[self.rear]  

    def add(self, obj):
        if self.is_full():
            raise Exception("QueueOverFlow")  
        else:  
            self.queue.append(obj)  
            self.rear += 1  

    def delete(self):
        if self.is_empty():
            raise Exception("QueueIsEmpty")  
        else:  
            self.rear -= 1
            return self.queue.pop(0)  

    def show(self):
        print(self.queue)  
        
if __name__ == "__main__":
    q = Queue(3)
    q.add(1)
    q.add(2)
    q.show()
    q.delete()
    q.show()
