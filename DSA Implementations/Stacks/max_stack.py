class MaxStack:
    def __init__(self):
        self.max_stack = []
        self.main_stack = []

    def push(self,data):
        self.main_stack.append(data)
        
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return
        
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])


    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()
    
    def get_max(self):
        return self.max_stack.pop()

mst = MaxStack()
mst.push(9)
mst.push(8)
mst.push(10)

print(mst.pop())

print(mst.get_max())
print(mst.pop())