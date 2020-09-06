# Class for creating a node in a binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
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

# Modified DFS code for finding the ancestors of a target node
def find_ancestor(root, search_node):
    # Condition check for the empty tree
    if root is None:
        return
    # Base condition if find the target node
    if root.data == search_node:
        return True
    # Recursive condition for finding the ancestor of the search node
    if (find_ancestor(root.left, search_node) or find_ancestor(root.right, search_node)):
        print(root.data)
        return 1
    return 0

if __name__ == "__main__":

    #Constructing the binary tree
    root = None
    root = insert_node(root, 20)
    root = insert_node(root, 25)
    root = insert_node(root, 15)
    root = insert_node(root, 10)
    root = insert_node(root, 18)
    root = insert_node(root, 24)
    root = insert_node(root, 28)
    root = insert_node(root, 10)
    root = insert_node(root, 65)
    root = insert_node(root, 8)
    root = insert_node(root, 5)

    # Initializing the search node parameter and calling the find ancestor function
    search_node = int(input())
    print ("The ancestor of node {} is as follows: ".format(search_node))
    if find_ancestor(root, search_node) !=1 :
        print("The target node {} is not present in the tree so no ancestors are possible: ".format(search_node))
