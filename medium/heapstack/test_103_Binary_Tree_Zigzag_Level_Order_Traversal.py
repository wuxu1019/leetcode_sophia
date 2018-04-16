"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lr = True
        rt = []
        queue = [root]
        while queue:
            new_queue = []
            data = []
            print lr
            while queue:
                p = queue.pop()
                data.append(p.val)
                if lr:
                    if p.left:
                        new_queue.append(p.left)
                    if p.right:
                        new_queue.append(p.right)
                else:
                    if p.right:
                        new_queue.append(p.right)
                    if p.left:
                        new_queue.append(p.left)
            lr = not lr
            rt.append(data)
            queue = new_queue
        return rt

