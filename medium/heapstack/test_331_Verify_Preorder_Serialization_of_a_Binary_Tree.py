"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        pl = preorder.split(',')
        while len(pl) > 1:
            ps = []
            a, b, c = 0, 1, 2
            while a < len(pl):
                if c < len(pl) and pl[b] == pl[c] == '#' and pl[a] != '#':
                    ps.append('#')
                    a, b, c = a + 3, b + 3, c + 3
                else:
                    ps.append(pl[a])
                    a, b, c = a + 1, b + 1, c + 1
            if len(ps) == len(pl):
                return False
            pl = ps
        return pl[0] == '#'

    def isValidSerialization_stack(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        stk = []
        for i in preorder:
            stk.append(i)
            while len(stk) >= 3 and stk[-1] == '#' and stk[-2] == '#' and stk[-3] != '#':
                stk.pop()
                stk.pop()
                stk.pop()
                stk.append('#')
        return len(stk) == 1 and stk[0] == '#'

if __name__ == '__main__':
    s = Solution()
    preorder = '9,3,4,#,#,1,#,#,2,#,6,#,#'
    rt1 = s.isValidSerialization_stack(preorder)
    print rt1

    preorder = '1,#,#,#,#'
    rt2 = s.isValidSerialization_stack(preorder)
    print rt2