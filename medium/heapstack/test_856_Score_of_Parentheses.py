"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
"""


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        stk = []
        for c in S:
            if c == '(':
                stk.append(c)
            elif c == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                    stk.append(1)
                else:
                    while len(stk) >= 2 and stk[-2] != '(':
                        data = stk.pop()
                        stk[-1] += data
                    sm = stk.pop()
                    stk[-1] = sm * 2
        return sum(stk)

