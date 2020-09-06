class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

# Applying DFS strategy for traversing the list
def recursive_count_leaves(root):
    # Base case of the recursion
    if root is None:
        return
    
    while root:
        count = 0
        if root.left is None and root.right is None:
            count +=1
            return count
        return recursive_count_leaves(root.left) + recursive_count_leaves(root.right)

# Applying BFS strategy for traversing
def iterative_count_leaves(root):
    if root is None:
        return
    count = 0
    queue = []
    queue.append(root)
    while len(queue) > 0:
        
        Node = queue.pop(0)
        # Condition for checking the parent nodes in a tree
        if Node.left != None:
            queue.append(Node.left)
        if Node.right != None:
            queue.append(Node.right)
        # Condition for checking the leaf_nodes
        if Node.left == None and Node.right == None:
            count += 1
    return count   




if __name__ == "__main__":

    root       = Node(50)
    root.left  = Node(45)
    root.right = Node(55)
    root.left.left = Node(25)
    root.left.right = Node(65)
    root.right.left = Node(75)
    root.right.right = Node(96)

    recursive_result = recursive_count_leaves(root)
    print ("There are total {} leaf nodes in the tree ".format(recursive_result)) 

    iterative_result = iterative_count_leaves(root)
    print ("There are total {} leaf nodes in the tree ".format(iterative_result)) 