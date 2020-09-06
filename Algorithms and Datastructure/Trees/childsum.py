class Node:
    def __init__(self, key):
        self.data  = key
        self.left  = None
        self.right = None

# Function for traversing the tree in traversal
def inorder(root):    
    if root is None:
        return
    inorder(root.left)
    print (root.data)
    inorder(root.right)

# Function for checking the child_sum
def check_child_sum(root):
    # Base case for the recursion
    if root is None or (root.left is None and root.right is None):
        return True
    l = 0
    r = 0
    # Iserting the left sum  
    if root.left != None:
        l = root.left.data
    if root.right != None:
        r = root.right.data
    # Recursive equation for finding the child_sum
    if ((root.data == l+r) and check_child_sum(root.left) and check_child_sum(root.right)):
        return True
    return False

if __name__ == "__main__":

    root      = Node(15)
    root.left = Node(10)
    root.right= Node(5)
    inorder(root)
    if(check_child_sum(root) is True):
        print("children sum property satisfied")
    else:
        print("not satisfy children sum property")
