
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        if d == 1:
            head = TreeNode(v)
            head.left = root
            return head
        stk, ct = [root], 1
        while ct < d - 1:
            nlayer = []
            while stk:
                p = stk.pop(0)
                if p.left:
                    nlayer.append(p.left)
                if p.right:
                    nlayer.append(p.right)
            stk = nlayer
            ct += 1
        while stk:
            p = stk.pop(0)
            templ, p.left = p.left, TreeNode(v)
            tempr, p.right = p.right, TreeNode(v)
            p.left.left, p.right.right = templ, tempr

        return root