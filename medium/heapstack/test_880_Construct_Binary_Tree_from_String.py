"""
Description
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
Have you met this question in a real interview?
Example
Given s = "4(2(3)(1))(6(5))", return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5
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
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        # write your code here
        i = 0
        stk = []
        while i < len(s):
            if s[i] == ')':
                stk.pop()
                i += 1
            elif s[i].isdigit() or s[i] == '-':
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                    j += 1
                node = TreeNode(int(s[i:j]))
                i = j
                if stk:
                    if not stk[-1].left:
                        stk[-1].left = node
                    else:
                        stk[-1].right = node
                stk.append(node)
            else:
                i += 1
        return stk[-1]