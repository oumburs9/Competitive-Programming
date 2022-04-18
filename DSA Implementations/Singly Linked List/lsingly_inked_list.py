class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.numNode = 0
    def insert_start(self,data):

        self.numNode += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self,data):
        self.numNode += 1
        new_node = Node(data)
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    def remove_node(self,data):
        
        current_node = self.head
        prev_node = None
        if not self.head:
            return

        while current_node.data != data and current_node:
            prev_node = current_node
            current_node = current_node.next
        

        if not current_node:
            return
        self.numNode -= 1
        if not prev_node:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next


        



    def size_of_list(self):
        return self.numNode
        

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

if __name__ == '__main__':
    llst = LinkedList()
    llst.insert_start(4)
    llst.insert_start(3)
    llst.insert_start(2)
    llst.insert_start(1)
    print('----------')
    llst.traverse()
    print("size:",llst.size_of_list())
    llst.remove_node(1)
    print('----------')
    llst.traverse()
    print('----------')
    llst.insert_end(8)
    llst.insert_start(10)

    llst.traverse()
    print('----------')
    print("size:",llst.size_of_list())
    print('----------')
    print('-----hh-----')
    llst.remove_node(8)
    llst.remove_node(10)

    llst.traverse()
    print('----------')
    print("size:",llst.size_of_list())


            
