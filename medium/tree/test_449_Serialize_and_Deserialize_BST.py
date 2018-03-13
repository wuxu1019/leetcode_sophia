"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        rt = []
        stk = [root]
        while stk:
            newstk = []
            while stk:
                p = stk.pop(0)
                if p == None:
                    rt.append('#')
                else:
                    rt.append(str(p.val))
                    newstk.extend([p.left, p.right])
            stk = newstk
        return ':'.join(rt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(':')
        head = TreeNode(data.pop(0))
        stk = [head]
        while data:
            newstk = []
            while stk:
                p = stk.pop(0)
                if data:
                    c = data.pop(0)
                    if c == '#':
                        p.left = None
                    else:
                        p.left = TreeNode(c)
                        newstk.append(p.left)
                if data:
                    c = data.pop(0)
                    if c == '#':
                        p.right = None
                    else:
                        p.right = TreeNode(c)
                        newstk.append(p.right)
            stk = newstk
        return head


class Codec2:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        rt = []

        def inorder(root):
            if not root:
                return
            rt.append(str(root.val))
            inorder(root.left)
            inorder(root.right)

        inorder(root)
        return ' '.join(rt)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        vals = collections.deque(int(i) for i in data.split())

        def buildTree(min, max):
            if vals and vals[0] > min and vals[0] < max:
                p = vals.popleft()
                node = TreeNode(p)
                node.left = buildTree(min, p)
                node.right = buildTree(p, max)
                return node

        return buildTree(-float('INF'), float('INF'))
