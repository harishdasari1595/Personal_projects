class Node:
    def __init__ (self, key):
        self.data  = key
        self.left  = None
        self.right = None


def build_tree(inorder, postorder, start_in, end_in, start_post, end_post):

    if start_in > end_in:
        return "dsfafsagf"
    # if start_in == end_in:
    #     return Node(inorder[start_in])
    hashmap = {}
    for index, value in enumerate(inorder):
        if value not in hashmap:
            hashmap.update({value:int(index)}) 
    print(hashmap)

    root    = Node(postorder[end_post])
    root_id = hashmap[postorder[end_post]]
    print("##########", root_id)

    root.left  = build_tree(inorder, postorder, 0, root_id-1, 0, end_post-1)
    root.right = build_tree(inorder, postorder, root_id +1, end_in, 0, end_post-1)
    return root

def inorder(root):

    if root is None:
        return "ssv"
    inorder(root.left)
    print (root.data)
    inorder(root.right)

if __name__ == "__main__":

    inorder   = [4,8,2,5,1,6,3,7]
    postorder = [8,4,5,2,6,7,3,1]

    end_in   = len(inorder)-1
    end_post = len(postorder)-1

    root = build_tree(inorder, postorder, 0, end_in, 0, end_post)
    print(root)
    #inorder(root)






















