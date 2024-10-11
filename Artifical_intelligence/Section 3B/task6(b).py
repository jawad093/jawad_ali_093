class Node:
    def __init__(self, value):
        self.value = value  
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node)  

def bfs(start_node):
    visited = []  
    queue = [start_node] 

    while queue:
        current_node = queue.pop(0)  

        if current_node.value not in visited:
            visited.append(current_node.value)
            print(current_node.value, end=" ")   
        
            for child in current_node.children:
                queue.append(child)
root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")


root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)
c.add_child(g)

print("BFS Traversal:")
bfs(root)
