"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rt = []

        def travesal(root, level):
            if not root:
                return
            if len(rt) - 1 < level:
                rt.append([root.val])
            else:
                rt[level].append(root.val)
            travesal(root.left, level + 1)
            travesal(root.right, level + 1)

        travesal(root, 0)
        return rt