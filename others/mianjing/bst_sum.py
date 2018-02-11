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
    print rt
    return rt
    
root = bstNode(1)
bstNode.left = bstNode(2)
bstNode.right = bstNode(3)
bstNode.left.left = 4
bstNode.left.right = 5
bstNode.right.left = 6
bstNode.right.right = 7
sm = sumBST(root, 2, 5)
print sm

