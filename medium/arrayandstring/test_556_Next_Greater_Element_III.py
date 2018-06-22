"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


Example 2:

Input: 21
Output: -1

"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = [int(i) for i in str(n)]
        target = -1
        i, j = 0, 0
        for i in range(len(c) - 1, 0, -1):
            if c[i - 1] < c[i]:
                target = c[i - 1]
                break
        if target < 0:
            return -1
        for j in range(len(c) - 1, i - 1, -1):
            if c[j] > target:
                break
        rt = c[:i - 1] + [c[j]] + sorted([target] + c[i:j] + c[j + 1:])
        ans = int(''.join([str(i) for i in rt]))
        print ans
        return -1 if ans > 2147483647 else ans
