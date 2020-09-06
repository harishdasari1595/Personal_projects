
class Node:
    def __init__(self, data):
        self.root  = data
        self.left  = None
        self.right = None


def is_siblings(root, a , b):
    
    # Base case for the recursion
    if root is None:
        return 0
    # Checking the sibling relationship (children from similar parent node).
    # First root node is checked whether a and b is the direct chidren of the root node.
    # Checking the nodes a and b is satisfy the sibling property in either LST or RST.   
    return ((((root.left == a) and root.right == b)) or ((root.left == b) and (root.right == a))or
             (is_siblings(root.left, a, b))  or (is_siblings(root.right, a ,b)))

def find_level(root, node, level):
    # Base case for the recursion
    if root is None:
        return 0
    if root  == node:  
        return level  
    # Finding the depth of the node in left subtree     
    depth = find_level(root.left, node, level+1)
    if depth != 0:
        return depth
    # Finding the depth of the node in the right subtree
    return find_level(root.right, node, level+1)

def is_cousin(root, a, b):
    
    # Condition for checking if the nodes are not siblings and are at similar level
    if ((find_level(root, a, 1) == find_level(root, b, 1)) and not(is_siblings(root, a, b))):
        print (find_level(root,a, 1), find_level(root, b, 1))
        return 1
    else:
        return 0

# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
# root.left.right = Node(5) 
# root.left.right.right = Node(15) 
# root.right.left = Node(6) 
# root.right.right = Node(7) 
# root.right.left.right = Node(8) 

node1 = root.left.right 
node2 = root.right.right  
  
if is_cousin(root, root.right, root.left.left) == 1:
    print ("yes")
else:
    print ("No")