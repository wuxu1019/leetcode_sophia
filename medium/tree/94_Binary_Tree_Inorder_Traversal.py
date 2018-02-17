"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

"""


class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        rt = []
        stk = [root]
        flag = True
        while stk:
            flag = True
            while stk[-1].left:
                stk.append(stk[-1].left)
            while flag and stk:
                p = stk.pop()
                rt.append(p.val)
                if p.right:
                    stk.append(p.right)
                    flag = False
        return rt
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
