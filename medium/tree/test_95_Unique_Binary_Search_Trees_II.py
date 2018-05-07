"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        self.memo = {}
        if not n:
            return []
        return self.dfs(range(1, n + 1), 0, n - 1)

    def dfs(self, nums, i, j):
        if i > j:
            return [None]
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        rt = []
        for p in range(i, j + 1):
            L = self.dfs(nums, i, p - 1)
            R = self.dfs(nums, p + 1, j)
            for l in L:
                for r in R:
                    nNode = TreeNode(nums[p])
                    nNode.left = l
                    nNode.right = r
                    rt.append(nNode)
        self.memo[(i, j)] = rt
        return rt


