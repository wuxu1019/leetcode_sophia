"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        return self.buildTreeHelper(0, len(inorder) - 1)

    def buildTreeHelper(self, s, e):
        if s > e:
            return None
        val = self.postorder.pop()
        root = TreeNode(val)
        index = self.inorder.index(val, s, e + 1)
        root.right = self.buildTreeHelper(index + 1, e)
        root.left = self.buildTreeHelper(s, index - 1)
        return root
