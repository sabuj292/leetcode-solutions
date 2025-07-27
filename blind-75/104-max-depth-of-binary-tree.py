class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

# Leaf nodes
node15 = TreeNode(15)
node7 = TreeNode(7)
node9 = TreeNode(9)

# Subtree rooted at 20
node20 = TreeNode(20, left=node15, right=node7)

# Root node
root = TreeNode(3, left=node9, right=node20)

# Run the function and print the result
print(maxDepth(root))  # Expected output: 3
