
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
        def lowestCommonAncestor(self, root, p, q):
                """
                :type root: TreeNode
                :type p: TreeNode
                :type q: TreeNode
                :rtype: TreeNode
                """
                path_p = self.findNode(root, p, [])
                path_q = self.findNode(root, q, [])

                i = 0
                while i < len(path_p) and i < len(path_q):
                        if i == len(path_q) - 1 and path_p[i] == path_q[i]:
                                return path_q[i]
                        if i == len(path_p) - 1 and path_p[i] == path_q[i]:
                                return path_p[i]
                        if path_p[i] == path_q[i] and path_p[i + 1] != path_q[i + 1]:
                                return path_p[i]
                        i += 1
                return None

        def findNode(self, root, node, path):
                if not root:
                        return []
                if root == node:
                        path.append(root)
                        return path
                rt = self.findNode(root.left, node, path + [root])
                if rt:
                        return rt
                rt = self.findNode(root.right, node, path + [root])
                return rt

        def lowestCommonAncestor_iteration(self, root, p, q):
                """
                :type root: TreeNode
                :type p: TreeNode
                :type q: TreeNode
                :rtype: TreeNode
                """
                stack = [root]
                parent = {root: None}
                while p not in parent or q not in parent:
                        node = stack.pop()
                        if node.left:
                                parent[node.left] = node
                                stack.append(node.left)
                        if node.right:
                                parent[node.right] = node
                                stack.append(node.right)
                path = set()
                while p:
                        path.add(p)
                        p = parent[p]
                while q not in path:
                        q = parent[q]
                return q

        def lowestCommonAncestor_recursive(self, root, p, q):
                """
                :type root: TreeNode
                :type p: TreeNode
                :type q: TreeNode
                :rtype: TreeNode
                """
                if root in (p, q, None):
                        return root
                left = self.lowestCommonAncestor(root.left, p, q)
                right = self.lowestCommonAncestor(root.right, p, q)

                if left and right:
                        return root
                if left:
                        return left
                if right:
                        return right
                return None

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(8)

    p = root.left
    q = root.right

    rt = s.lowestCommonAncestor(root, p, q)
    print rt