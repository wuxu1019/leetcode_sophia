"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum_dfs(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.rt = []

        def pathSumHelper(root, base, left):
            if not root:
                return
            if not root.left and not root.right:
                if left == root.val:
                    self.rt.append(base + [root.val])
                return
            base.append(root.val)
            exleft = left - root.val
            pathSumHelper(root.left, base, exleft)
            pathSumHelper(root.right, base, exleft)
            base.pop()

        pathSumHelper(root, [], sum)
        return self.rt

    def pathSum_bfs(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        rt = []
        queue = collections.deque([(root, [], 0)])

        while queue:
            node, base, c = queue.popleft()
            temp = c + node.val
            if not node.left and not node.right and temp == sum:
                rt.append(base + [node.val])
            if node.left:
                queue.append([node.left, base + [node.val], temp])
            if node.right:
                queue.append([node.right, base + [node.val], temp])
        return rt

