class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert_left(self, current_node, data):
        current_node.left = Node(data)

    def insert_right(self, current_node, data):
        current_node.right = Node(data)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)    
            self.preorder(node.right)   

    def inorder(self, node):
        if node:
            self.inorder(node.left)   
            print(node.data, end=" ")   
            self.inorder(node.right)    

    def postorder(self, node):
        if node:
            self.postorder(node.left)   
            self.postorder(node.right)  
            print(node.data, end=" ")    


tree = BinaryTree("a")
tree.insert_left(tree.root, "b")
tree.insert_right(tree.root, "c")
tree.insert_left(tree.root.left, "d")
tree.insert_right(tree.root.left, "e")
tree.insert_left(tree.root.right, "f")
tree.insert_right(tree.root.right, "g")

print("Preorder Traversal:")
tree.preorder(tree.root)
print("\nInorder Traversal:")
tree.inorder(tree.root)
print("\nPostorder Traversal:")
tree.postorder(tree.root)
