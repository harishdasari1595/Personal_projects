
class Node:

    def __init__ (self, key):

        self.data  = key
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

# Function for performing level order traversal    
def level_order_traversal(root):
    # Condition if tree is empty
    if root is None:
        return
    # Queue for storing the nodes at each level of the tree
    queue = []
    queue.append(root)
    
    # Traversing the nodes in a level order 
    while (len(queue) > 0):
        
        print (queue[0].data)
        Node = queue.pop(0)

        if Node.left is not None:
            queue.append(Node.left)

        if Node.right is not None:
            queue.append(Node.right)

if __name__ == "__main__":

    root = None
    root = insert_node(root, 15)
    root = insert_node(root, 12)
    root = insert_node(root, 20)
    root = insert_node(root, 10)
    root = insert_node(root, 18)

    # Calling the levelorder traversal
    level_order_traversal(root)



    