"""
give a BST, and min & max, 
get the sum of BST val, which in the range of min <= val <= max
"""
class bstNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumBST(root, min, max):
    if not root:
        return 0
    if root.val >= min and root.val <= max:
        rt = root.val
    else:
        rt = 0
    rt += sumBST(root.left, min, max) + sumBST(root.right, min, max)
    return rt
    
root = bstNode(1)
root.left = bstNode(2)
root.right = bstNode(3)
root.left.left = bstNode(4)
root.left.right = bstNode(5)
root.right.left = bstNode(6)
root.right.right = bstNode(7)
sm = sumBST(root, 2, 5)
print sm

