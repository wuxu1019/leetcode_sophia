# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree_copy(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        rval = preorder[0]
        root = TreeNode(rval)
        index = inorder.index(rval)
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

    def buildTree_index(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = collections.deque(preorder)
        self.inorder = inorder

        return self.buildTreeHelper(0, len(preorder) - 1)

    def buildTreeHelper(self, start, end):
        if start > end:
            return None
        rval = self.preorder.popleft()
        root = TreeNode(rval)
        i = self.inorder.index(rval, start, end + 1)
        root.left = self.buildTreeHelper(start, i - 1)
        root.right = self.buildTreeHelper(i + 1, end)
        return root

    def buildTree_trick(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()

        return build(None)
