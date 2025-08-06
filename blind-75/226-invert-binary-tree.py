# problem description
# we are given a root of a binary tree and we have to
    # Invert (or mirror) the tree and return the root of the inverted tree
    
    # Inverting means ------> just swapping the left and right subtrees at every node
    
class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        # swap left and right
        root.left, root.right = root.right, root.left
        
        # recursive call
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root