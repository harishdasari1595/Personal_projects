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
    if root == x or root == y:
        return root
    
    leftsearch  = LCA(root.left, x, y)
    rightsearch = LCA(root.right, x, y)

    if leftsearch == None:
        return rightsearch
    if rightsearch == None:
        return leftsearch 

    return root

if __name__ == "__main__":

    root=None
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.left=Node(60) 
    root.right.right=Node(70)
    root.left.left.left= Node(80)
    root.left.left.right= Node(90)
    root.left.right.left= Node(100)
    root.left.right.right= Node(110)
    # Taking input from the user 
    x, y = [int(value) for value in input().split()]
    node =LCA(root, x ,y)
    print ("Least common ancestor of {} and {} is {} ".format(x,y, node.data))


    
