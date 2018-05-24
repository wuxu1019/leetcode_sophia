"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].

"""


class Solution(object):
    def checkValidString_greedy(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, high = 0, 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low = max(0, low - 1)
                high -= 1
            else:
                low = max(0, low - 1)
                high += 1
            if high < 0:
                return False
        return low == 0

    def checkValidString_stk(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_left, stack_star = [], []
        for i, c in enumerate(s):
            if c == '(':
                stack_left.append(i)
            elif c == '*':
                stack_star.append(i)
            else:
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        i, j = len(stack_left) - 1, len(stack_star) - 1
        while i >= 0 and j >= 0:
            if stack_star[j] > stack_left[i]:
                i, j = i - 1, j - 1
                stack_left.pop()
            else:
                j = j - 1
        if stack_left:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    l = "(*))"
    rt1 = s.checkValidString_greedy(l)
    rt2 = s.checkValidString_stk(l)
    print rt1
    print rt2