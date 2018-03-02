"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stk = [root]
        rt = []
        while stk:
            p = stk.pop()
            rt.append(p.val)
            if p.right:
                stk.append(p.right)
            if p.left:
                stk.append(p.left)
        return rt

        """
        :type root: TreeNode
        :rtype: List[int]
        """
