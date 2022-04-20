from multiprocessing import parent_process


class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            self.root = Node(data)
        else:
            self.root = self.insert_node(data, self.root)
    def insert(self,data,node):
        if data < node.data:
            if self.leftChild:
                self.insert_node(data,node.leftChild)
            else:
                node.leftChild = Node(data,node)
        else:
            if self.rightChild:
                self.insert_node(data,node.rightChild)
            else:
                node.rightChild = Node(data,node)
                

