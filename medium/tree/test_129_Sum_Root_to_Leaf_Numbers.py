"""

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


"""


class Solution(object):
    def sumNumbers_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfsSum(root, base):
            if not root:
                return 0
            rt = base * 10 + root.val
            if not root.left and not root.right:
                return rt
            else:
                return dfsSum(root.left, rt) + dfsSum(root.right, rt)

        return dfsSum(root, 0)

    def sumNumbers_recuisive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stk = [(root, 0)]
        s = 0
        while stk:
            p = stk.pop()
            if p[0]:
                base = p[1] * 10 + p[0].val
                if not p[0].left and not p[0].right:
                    s += base
                else:
                    stk.append((p[0].left, base))
                    stk.append((p[0].right, base))

        return s

    def sumNumbers_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0)]
        s = 0
        for rt, pre in queue:
            if rt:
                base = rt.val + pre * 10
                if not rt.left and not rt.right:
                    s += base
                else:
                    queue.append((rt.left, base))
                    queue.append((rt.right, base))
        return s
