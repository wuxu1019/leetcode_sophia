"""
Description
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example
Given
  1
   \
    2
   / \
  3   4

return
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].



"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """

    def boundaryOfBinaryTree(self, root):
        # write your code here
        mark = root

        left, mid, right = [], [], []

        while root.left or root.right:
            while root.left:
                left.append(root.val)
                root = root.left
            if root.right:
                left.append(root.val)
                root = root.right

        def dfs(root, base):
            if not root:
                return base
            if not root.left and not root.right:
                base.append(root.val)
                return base
            base = dfs(root.left, base)
            base = dfs(root.right, base)
            return base

        mid = dfs(mark, mid)

        root = mark.right
        while root and (root.left or root.right):
            while root.right:
                right.append(root.val)
                root = root.right
            if root.left:
                right.append(root.val)
                root = root.left
        return left + mid + right[::-1]

