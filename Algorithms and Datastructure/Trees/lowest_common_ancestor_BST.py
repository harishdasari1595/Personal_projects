class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

# Function for inserting nodes into the binary tree 
def insert_node(root, data):
    # Condition check for empty tree
    if root is None:
        root = Node(data)
    # Inserting nodes smaller values in the left subtree
    if data < root.data:
        root.left =  insert_node(root.left, data)
    # Inserting nodes larger values in the right subtree
    if data > root.data:
        root.right = insert_node(root.right, data)
    return root

# Function for finding the Least common ancestor of x and y 
# Modified DFS implementation
def LCA(root, x, y):
    # Base case for the recursion 
    if root is None:
        return
    # Recursive equation for finding the LCA
    if root.data > x and root.data > y:
        return LCA(root.left, x, y)
    elif root.data < x and root.data < y:
        return LCA(root.right, x, y)

    return root

if __name__ == "__main__":

    root = None
    root = insert_node(root, 20)
    root = insert_node(root, 8)
    root = insert_node(root, 22)
    root = insert_node(root, 4)
    root = insert_node(root, 12)
    root = insert_node(root, 10)
    root = insert_node(root, 14)

    # Taking input from the user 
    x, y = [int(value) for value in input().split()]
    node =LCA(root, x ,y)
    print ("Least common ancestor of {} and {} is {} ".format(x,y, node.data))


    
