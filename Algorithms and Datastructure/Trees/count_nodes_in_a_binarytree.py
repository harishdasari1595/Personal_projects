
class Node:
    def __init__(self, key):
        self.left  = None
        self.data  = key
        self.right = None
        self.rightThread = False

##############################################################
# Recursive code for counting the number of nodes in a tree
##############################################################
def count_nodes(root):

    if root is None:
        return 0
    return (1 + (count_nodes(root.left) + count_nodes(root.right)))

###############################################################
# Iterative approach for counting the number of nodes in a tree
###############################################################
# Function for finding the leftmost node
def leftmost(node):

    while node is not None and node.left is not None:
        node  = node.left
    return node
# Iterative approach for counting the nodes in a binary tree
# Function for performing an inorder traversal
def inorder(root):

    if root is None:
        return
    # Finding the leftmost node
    curr = leftmost(root)

    while curr != None:
        print ("current node", curr.data)

        if curr.rightThread != True: 
            print ("!!!!!!!!!!!!!!!!!")
            curr = curr.right
            print(curr.data)
        else:
            curr = leftmost(curr.right)
    print("\n")

if __name__ == "__main__":

    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    root.right.right = Node('G')
    root.left.left.left = Node('H')
    root.left.left.right = Node('I')
    root.right.left.right = Node('J')

print ("-------------------------")
#inorder(root)
print(count_nodes(root))



