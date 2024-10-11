
tree = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": [],
    "e": [],
    "f": [],
    "g": []
}

visited = []  

def bfs(start, goal):
    current_level = [start]  

    while current_level:
        next_level = []  

        for node in current_level:
            if node not in visited:
                visited.append(node) 
                print(node, end=" ")   
            
            
            next_level.extend(tree[node])  

        current_level = next_level 

bfs('a', 'g')
print("\nVisited nodes:", visited)
