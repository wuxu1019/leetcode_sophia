"""
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

Have you met this question in a real interview?
Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        rt = []

        def travesal(root, rt):
            if not root:
                rt.append('#')
                return
            rt.append(str(root.val))
            travesal(root.left, rt)
            travesal(root.right, rt)

        travesal(root, rt)
        return ' '.join(rt)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here

        l = data.split(' ')
        stk = []
        for c in l:
            if c == '#':
                if not stk:
                    return None
                else:
                    if stk[-1].left == '#':
                        stk[-1].left = None
                    else:
                        stk[-1].right = None
                        stk.pop()
            else:
                node = TreeNode(int(c))
                node.left, node.right = '#', '#'
                if not stk:
                    root = node
                    stk.append(node)
                else:
                    if stk[-1].left == '#':
                        stk[-1].left = node
                    else:
                        stk[-1].right = node
                        stk.pop()
                    stk.append(node)
        return root
