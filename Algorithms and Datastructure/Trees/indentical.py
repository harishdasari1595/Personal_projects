class Node:

    def __init__(self, key):
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

# Recursive check for checking the trees are identical or not
def identical_check(root1 , root2):
    # Base case for the recursion
    if root1 is None and root2 is None:
        return
    # Recurseive equation of the identical check
    if root1 and root2:
        return(root1.data == root2.data and identical_check(root1.left, root2.left) 
                and identical_check(root1.right, root2.right))



if __name__ == "__main__":

    # Constructing nodes of the binary tree
    root1 = None
    root2 = None
    root1 = insert_node(root1, 15)
    root1 = insert_node(root1, 12)
    root1 = insert_node(root1, 20)
    root1 = insert_node(root1, 10)
    root1 = insert_node(root1, 18)
    root2 = insert_node(root2, 15)
    root2 = insert_node(root2, 12)
    root2 = insert_node(root2, 20)
    root2 = insert_node(root2, 10)
    root2 = insert_node(root2, 18)
 
    if identical_check:
        print ("Both the trees are identical")
    else:
        print ("Both the trees are not identical")


