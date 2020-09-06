 
class Node:
    def __init__(self, key):
        self.data  = key
        self.left  = None
        self.right = None 

def make_sumtree(root):

    if root is None:
        return
    
    oldval=root.data
    
    root.info=make_sumtree(root.left) + make_sumtree(root.right)
    
    return root.info + oldval

def inorder(root):
    
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

if __name__ == "__main__":

    root = Node(20)
    root.left = Node(42)
    root.right = Node(26)
    root.left.right = Node(14)
    root.left.left = Node(15)
    root.right.left = Node(85)
    root.right.right = Node(75)

    inorder(root)
    root = make_sumtree(root)
    inorder(root)
