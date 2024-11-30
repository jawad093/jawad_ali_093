class Node:
    def __init__(self, data):
        self.data = data
        self.children = [] 

    def add_child(self, child_node):
        self.children.append(child_node)  

def DFS(initial_node, target_value):
    stack = [initial_node]  
    visited = []  

    while stack:
        current_node = stack.pop()  

        if current_node.data not in visited:
            visited.append(current_node.data)  
            print(current_node.data, end=" ")  

            if current_node.data == target_value:  
                return

            for child in current_node.children:  
                stack.append(child)


Starting_root = Node("LAHore")
faslabad = Node("faslabad")
karachi = Node("karachi")
multan = Node("multan")
chock = Node("chock")
feroz = Node("feroz")


Starting_root.add_child(faslabad)
Starting_root.add_child(karachi)
faslabad.add_child(multan) 
karachi.add_child(chock)    
chock.add_child(feroz)      


DFS(Starting_root, 'feroz')
