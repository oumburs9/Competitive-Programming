class Queue:
    def __init__(self):
        self.stack = []
    def enqueue(self,data):
        self.stack.append(data)
    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeued_item = self.dequeue()

        self.stack.append(item)

        return dequeued_item


que = Queue()
que.enqueue(9)
que.enqueue((8))
print(que.dequeue())
