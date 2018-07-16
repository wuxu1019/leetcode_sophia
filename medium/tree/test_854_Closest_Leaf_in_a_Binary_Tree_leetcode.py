"""
Description
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.If there is more than one answer, return to the leftmost.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

1.root represents a binary tree with at least 1 node and at most 1000 nodes.
2.Every node has a unique node.val in range [1, 1000].
3.There exists some node in the given binary tree for which node.val == k.

Have you met this question in a real interview?
Example
Example 1:

Given:
root = {1, 3, 2}, k = 1
Diagram of binary tree:
          1
         / \
        3   2

Return: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Given:
root = {1}, k = 1
Return: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Given:
root = {1,2,3,4,#,#,#,5,#,6}, k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Return: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
DifficultyMedium
Total Accepted98
Total Submitted211
Accepted Rate45%
 Company

"""

"""
Definition of TreeNode:
"""
import  collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """

    def findClosestLeaf(self, root, k):
        # Write your code here
        if not root:
            return None

        self.rount = None

        def dfs(base, rt, target):
            base.append(rt)
            if rt.val == target:
                self.rount = base
                return True
            if rt.left and dfs(base, rt.left, target):
                return True
            if rt.right and dfs(base, rt.right, target):
                return True
            return False

        dfs([], root, k)
        minPath, rt = self.findMinPath(self.rount[-1])
        if minPath == 0:
            return rt.val

        inc = 1
        for i in range(len(self.rount) - 2, -1, -1):
            if self.rount[i + 1] == self.rount[i].left:
                path, node = self.findMinPath(self.rount[i].right)
                path += inc
            else:
                path, node = self.findMinPath(self.rount[i].left)
                path += inc
            if path < minPath:
                minPath = path
                rt = node
            inc += 1
        return rt.val

    def findMinPath(self, rt):
        if not rt:
            return float('INF'), None
        queue = collections.deque([(0, rt)])
        while queue:
            lth, node = queue.popleft()
            if not node.left and not node.right:
                return lth, node
            if node.left:
                queue.append((lth + 1, node.left))
            if node.right:
                queue.append((lth + 1, node.right))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(2)
    root.left.left.left.left = TreeNode(8)
    root.left.left.left.right = TreeNode(9)
    k = 2
    rt = s.findClosestLeaf(root, k)
    print rt

