# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
    
    
    
    # need to recap the problem and the solution
    
    # here "isSubtree()"
        # Traverse every node in root
        # At each node, call isSameTree() to check for exact match
        
    # isSameTree()
        # Recursively check if both trees are:
            # structurally identical
            # all node values match