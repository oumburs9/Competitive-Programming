class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def depth_first_search_iter(start_node):
    stack = [start_node]

    while stack:

        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                stack.append(n)

def depth_first_search_rec(node):

    node.visited = True
    print(node.name)

    for n in node.adjacency_list:
        if not n.visited:
            depth_first_search_rec(n)




if __name__ == '__main__':
    node1 = Node("J")
    node2 = Node("A")
    node3 = Node("B")
    node4 = Node("I")
    node0 = Node(1)
    node01 = Node(2)
    node5 = Node("R")


    node1.adjacency_list.append(node2)
    node2.adjacency_list.append(node3)
    node3.adjacency_list.append(node5)
    node5.adjacency_list.append(node0)
    node0.adjacency_list.append(node01)
    node3.adjacency_list.append(node4)


    print("iter")
    depth_first_search_iter(node1)
    # print("re")
    # depth_first_search_rec(node1)