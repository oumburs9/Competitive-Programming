class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def getNode(self, index: int) -> Node:
        if index < 0:
            return None
        cur = self.head
        for _ in range(index):
            if cur:
                cur = cur.next
            else:
                return None
        return cur
    
    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        
        prev_node = self.getNode(index - 1)
        if not prev_node:
            return
        new_node = Node(val)
        new_node.next = prev_node.next
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        node = self.getNode(index)
        if not node:
            return
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.prev = prev_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)