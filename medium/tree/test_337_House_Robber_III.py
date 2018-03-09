"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.head = None

    def constructTree(self, l):
        if not l:
            return self.head

        self.head = pt = TreeNode(l.pop(0))
        stk = [pt]
        while l:
            left = l.pop(0)
            right = l.pop(0) if l else None
            node = stk.pop(0)
            node.left = TreeNode(left) if left else None
            node.right = TreeNode(right) if right else None

            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return self.head


class Solution(object):
    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        if root.left:
            count += self.rob1(root.left.left) + self.rob1(root.left.right)
        if root.right:
            count += self.rob1(root.right.left) + self.rob1(root.right.right)
        po = self.rob1(root.left) + self.rob1(root.right)
        return max(root.val + count, po)

    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            """ record[0] means include root, record[1] means not include root"""
            if not root:
                return [0, 0]
            left, right = helper(root.left), helper(root.right)
            includeroot = root.val + left[1] + right[1]
            excluderoot = max(left[0], left[1]) + max(right[0], right[1])
            return [includeroot, excluderoot]

        return max(helper(root))

    def rob3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        record = {}
        def helper(root):
            if not root:
                return 0
            if root in record:
                return record[root]
            count = 0
            if root.left:
                count += self.rob3(root.left.left) + self.rob3(root.left.right)
            if root.right:
                count += self.rob3(root.right.left) + self.rob3(root.right.right)
            po = self.rob1(root.left) + self.rob1(root.right)
            record.setdefault(root, po)
            return max(root.val + count, po)

        return helper(root)

if __name__ == '__main__':
    tree = Tree()
    root = tree.constructTree([100,2,2,None,3,None,1, None,10])
    s = Solution()
    maxm1 = s.rob1(root)
    maxm2 = s.rob2(root)
    maxm3 = s.rob3(root)
    print maxm1, maxm2, maxm3
