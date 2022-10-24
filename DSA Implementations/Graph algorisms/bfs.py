class Node:
    def __init__(self,name):
        self.name = name
        self.adjecencyList = []
        self.visited = False

def breadth_first_search(start_node):
    queue = [start_node]
    start_node.visited = True 



    while queue:
        actual_node = queue.pop(0)
        print(actual_node.name)


        for n in actual_node.adjecencyList:
            if not n.visited:
                n.visited = True
                queue.append(n)


if __name__ == '__main__':
    node1 = Node("J")
    node2 = Node("A")
    node3 = Node("B")
    node4 = Node("I")
    node5 = Node("R")


    node1.adjecencyList.append(node2)
    node2.adjecencyList.append(node3)
    node3.adjecencyList.append(node4)
    node4.adjecencyList.append(node5)


    breadth_first_search(node1)


