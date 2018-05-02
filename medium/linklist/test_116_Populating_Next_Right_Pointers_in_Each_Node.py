"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_dfs(self, root):
        self.rightmost = []

        def dfs(root, level):
            if not root:
                return None
            if len(self.rightmost) < level:
                root.next = None
                self.rightmost.append(root)
            else:
                root.next = self.rightmost[level - 1]
                self.rightmost[level - 1] = root
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 1)

    def connect_o1_space(self, root):
        if not root:
            return root
        root.next = None
        while root and root.left:
            left = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                root = root.next
            root = left

