class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self,data):
        new_node =Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def traverse_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev
if __name__=='__main__':
    dll = DoublyLinkedList()
    dll.insert_end(5)
    dll.insert_end(1)
    dll.insert_end(6)
    dll.insert_end(8)

    dll.traverse_forward()
    print('---------------')
    dll.traverse_backward()
