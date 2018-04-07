"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""


class Solution(object):
    def widthOfBinaryTree_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = []
        self.rt = 0

        def dfs(root, pos, level):
            if not root:
                return
            if len(left) < level + 1:
                left.append(pos)
            self.rt = max(self.rt, pos - left[level] + 1)
            dfs(root.left, pos * 2 + 1, level + 1)
            dfs(root.right, pos * 2 + 2, level + 1)

        dfs(root, 0, 0)
        return self.rt

    def widthOfBinaryTree_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0, 0)]
        level_pre = -1
        count = 0
        for rt, pos, level in queue:
            if rt:
                queue.append((rt.left, pos * 2 + 1, level + 1))
                queue.append((rt.right, pos * 2 + 2, level + 1))
                if level != level_pre:
                    left = pos
                    level_pre = level
                count = max(count, pos - left + 1)
        return count