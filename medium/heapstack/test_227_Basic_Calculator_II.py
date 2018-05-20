"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""
import collections

class Solution(object):
    def calculate_bf(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = collections.deque()
        start = -1
        for i, c in enumerate(s):
            if c != ' ':
                if c.isdigit():
                    if start == -1:
                        start = i
                    if i == len(s) - 1 or not s[i + 1].isdigit():
                        l.append(int(s[start:i + 1]))
                        start = -1
                else:
                    l.append(c)
        l_n = collections.deque()
        while l:
            c = l.popleft()
            if c == '*':
                l_n.append(l_n.pop() * l.popleft())
            elif c == '/':
                l_n.append(l_n.pop() / l.popleft())
            else:
                l_n.append(c)
        while l_n:
            c = l_n.popleft()
            if c == '+':
                l.append(l.pop() + l_n.popleft())
            elif c == '-':
                l.append(l.pop() - l_n.popleft())
            else:
                l.append(c)
        return l[0]

    def calculate_stack(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        stk = []
        num = 0
        sign = '+'
        for i, c in enumerate(s):
            if c != ' ':
                if c.isdigit():
                    if start == -1:
                        start = i
                    if i == len(s) - 1 or not s[i + 1].isdigit():
                        num = int(s[start:i + 1])
                        start = -1
                        if sign == '*':
                            stk.append(stk.pop() * num)
                        elif sign == '/':
                            temp = stk.pop()
                            if temp < 0 and temp % num != 0:
                                stk.append(temp / num + 1)
                            else:
                                stk.append(temp / num)
                        elif sign == '-':
                            stk.append(-num)
                        elif sign == '+':
                            stk.append(num)
                else:
                    sign = c
        return sum(stk)

if __name__ == '__main__':
    s = Solution()
    l = '2*3 + 12222/4'
    rt1 = s.calculate_bf(l)
    rt2 = s.calculate_stack(l)

    print rt1
    print rt2
