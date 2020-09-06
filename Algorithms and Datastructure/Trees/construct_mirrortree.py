
class  Node:
    def __init__(self, x):
        self.data  = x
        self.left  = None
        self.right = None

# Function for inserting the nodes in the binary tree
def insert_node(root, data):

    if root is None:
        root = Node(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    if data > root.data:
        root.right = insert_node(root.right, data)
    return root

# Function for constructing the mirror of the tree
def construct_mirrortree(root):

    if root is None:
        return "#####"
    else:
        # Performing DFS
        construct_mirrortree(root.left)
        construct_mirrortree(root.right)
        # Swapping the left and right nodes
        temp=root.left
        root.left=root.right
        root.right=temp
        
# Function for performing the inorder traversal
def inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print  (root.data)
    inorder(root.right)

if __name__ == "__main__":

    root = None
    root = insert_node(root,10)
    root = insert_node(root,5)
    root = insert_node(root,15)
    root = insert_node(root,30)
    print("Original Tree")
    inorder(root)
    construct_mirrortree(root)
    print("Tree after mirroring")
    inorder(root)



