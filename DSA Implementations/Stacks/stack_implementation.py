
from threading import stack_size


class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack_size() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_stack(self):
        return len(self.stack)
        
    def is_empty(self):
        return self.stack == []
stack = Stack()
stack.push(1)
stack.push(11)
stack.push(111)
stack.push(1111)
print("size: %d" % stack.size_stack())
print("pop.: %d" % stack.pop())
print("size: %d" % stack.size_stack())
print("peek: %d" % stack.peek())
print("size: %d" % stack.size_stack())

