"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findKthNode(root, k):

    def dfs(root, n, k, base):
        if not root:
            return n, base, False

        n, base, found = dfs(root.right, n, k, base)
        if found:
            return n, base, True

        n += 1
        if n == k:
            return n, root.val, True

        base = root.val
        n, base, found = dfs(root.left, n, k, base)
        if found:
            return n, base, True

        return n, base, False

    n, base, found = dfs(root, 0, k, float('INF'))

    if found:
        return base
    else:
        return -1

if __name__ == '__main__':
    k = 1
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)


    rt = findKthNode(root, k)
    print rt


