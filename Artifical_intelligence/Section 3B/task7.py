class Node:
    def __init__(self, position):
        self.position = position  
        self.g = 0  
        self.h = 0  
        self.f = 0  
        self.parent = None  

    def __eq__(self, other):
        return self.position == other.position

def heuristic(node_position, goal_position):
    return abs(node_position[0] - goal_position[0]) + abs(node_position[1] - goal_position[1])

def astar(start, goal, grid):
    open_list = [] 
    closed_list = []  

    start_node = Node(start)
    goal_node = Node(goal)
    open_list.append(start_node)

    while open_list:
        current_node = open_list[0]
        for node in open_list:
            if node.f < current_node.f:
                current_node = node

        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  

        (x, y) = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] 

        for next_position in neighbors:
            if (next_position[0] < 0 or next_position[0] >= len(grid) or
                next_position[1] < 0 or next_position[1] >= len(grid[0]) or
                grid[next_position[0]][next_position[1]] == 1):
                continue  

            neighbor_node = Node(next_position)
            if neighbor_node in closed_list:
                continue 

            
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)  
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            neighbor_node.parent = current_node

            
            if add_to_open(open_list, neighbor_node):
                open_list.append(neighbor_node)

    return None  

def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor.position == node.position and neighbor.g >= node.g:
            return False
    return True

grid = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
]

start = (0, 0)  
goal = (4, 4)   


path = astar(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found.")
