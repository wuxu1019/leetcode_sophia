"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

"""

class Solution(object):
    def rightSideView_bfs1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view

    def rightSideView_dfs1(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            self.rt = {}

            def helper(root, base):
                if not root:
                    return
                self.rt.setdefault(base, root.val)
                helper(root.right, base + 1)
                helper(root.left, base + 1)

            helper(root, 0)
            return [self.rt[i] for i in sorted(self.rt.keys())]

