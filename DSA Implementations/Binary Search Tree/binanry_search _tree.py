class Node:
    def __init__(self,data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if  self.root is None:
            self.root = Node(data,None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self,data,node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data,node.leftChild)
            else:
                node.leftChild = Node(data,node)
        else:
            if node.rightChild:
                self.insert_node(data,node.rightChild)
            else:
                node.rightChild = Node(data,node)
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
    def traverse_in_order(self,node):

        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print("%s" % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

bst = BinarySearchTree()
bst.insert(1)
bst.insert(7)
bst.insert(4)
bst.insert(-3)

bst.traverse()


