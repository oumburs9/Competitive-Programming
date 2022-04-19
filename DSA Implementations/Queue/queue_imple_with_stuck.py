class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self,data):
        self.enqueue_stack.append(data)
    def dequeue(self):
        if (len(self.enqueue_stack) == 0) and (len(self.dequeue_stack) == 0):
            raise Exception("The stack is empty.")

        if len(self.dequeue_stack) == 0:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
que = Queue()
que.enqueue(9)
que.enqueue((8))
print(que.dequeue())
