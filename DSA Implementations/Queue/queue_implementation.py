class Queue:
    def __init__(self):
        self.queue = []
    def queue_size(self):
        return len(self.queue)
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue_size() < 1:
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data
    def peek(self):
        return self.queue[0]
que = Queue()
que.enqueue(1)
que.enqueue(9)
print("size: %d" %que.queue_size())
que.dequeue()
print("size: %d" %que.queue_size())
print("peek: %d" %que.peek())
print("size: %d" %que.queue_size())