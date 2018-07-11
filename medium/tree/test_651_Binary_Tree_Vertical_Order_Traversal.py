"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""


class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """

    def verticalOrder(self, root):
        # write your code here
        if not root:
            return []
        mp = collections.defaultdict(list)

        queue = collections.deque([(root, 0)])

        while queue:
            p, pos = queue.popleft()
            mp[pos].append(p.val)
            if p.left:
                queue.append((p.left, pos - 1))
            if p.right:
                queue.append((p.right, pos + 1))
        return [mp[i] for i in sorted(mp.keys())]
