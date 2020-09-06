
class Node:
    def __init__(self, x):
        self.data  = x
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

# Function for traversing the tree in a spiral form
def spiral_traversal(root):
    
    # Empty tree check 
    if root is None:
        return
    # Creating the stacks for storing the even and odd level nodes
    even_stack = []
    odd_stack  = []
    odd_level  = 1
    even_level = 2

    # Adding the root node to the odd stack as it is in the odd level
    odd_stack.append(root)

    # Loop for traversing the tree in a spiral form
    while len(even_stack) > 0 or len(odd_stack) > 0:

        print("printing {} level nodes of the tree".format(odd_level))
        # Loop for printing the odd level nodes and adding the even level nodes to the even stack
        while len(odd_stack) > 0:
            # Poping the nodes in Left to right order format
            node = odd_stack.pop(-1)
            print(node.data)

            # Pushing nodes into the even node in right to left order
            if node.right is not None:
                even_stack.append(node.right)
            if node.left is not None:
                even_stack.append(node.left)
            odd_level += 2
        
        print("printing {} level nodes of the tree".format(even_level))
        # Loop for printing the even level nodes and adding the odd level nodes to the odd stack
        while len(even_stack) > 0:
            # Poping the nodes in right to left order format
            node = even_stack.pop(-1) 
            print (node.data)

            # Pushing nodes into the odd node in left to right order
            if node.left is not None:
                odd_stack.append(node.left)
            if node.right is not None:
                odd_stack.append(node.right)
            even_level += 1

if __name__ == "__main__":
    
    # Constructing the tree 
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
    # Calling the spiral traversal function
    spiral_traversal(root)












