class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left,  q.left) and isSameTree(p.right, q.right)


# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(3)

# q = TreeNode(1)
# q.left = TreeNode(1)
# q.right = TreeNode(3)


# Tree p: left child
p = TreeNode(1)
p.left = TreeNode(2)

# Tree q: right child
q = TreeNode(1)
q.right = TreeNode(2)

print(isSameTree(p, q))  # Output: False


p = None
q = None
print(isSameTree(p, q))  # Output: True

p = TreeNode(1)
q = None
print(isSameTree(p, q))  # Output: False

p = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))

q = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7)))

print(isSameTree(p, q))  # Output: True


