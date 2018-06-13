"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

def count_universal_tree(root):
    ct = 0

    def count_universal_tree_helper(root):
        if not root:
            return True
        if not root.left and not root.right:
            ct += 1
            return True
        rt = True
        if root.left and (root.val != root.left.val or count_universal_tree_helper(root.left)):
            rt = False
        if root.right and (root.val != root.right.val or count_universal_tree_helper(root.right)):
            rt = False
        return rt

    count_universal_tree_helper(root)
    return ct