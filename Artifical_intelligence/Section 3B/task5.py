class Node:
    def __init__(self, data):
        self.data = data
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node)  


def dfs(start_node, goal):
    stack = [start_node]  
    visited = []  

    while stack:
        current_node = stack.pop()
        
        if current_node.data not in visited:
            visited.append(current_node.data) 
            
            print(current_node.data, end=" ")  
            
            if current_node.data == goal:  
                return

      
            for child in current_node.children:
                stack.append(child)


Starting_root = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


Starting_root.add_child(b)
Starting_root.add_child(c)
b.add_child(d)

c.add_child(e)
c.add_child(f) 

dfs(Starting_root, 'f')
