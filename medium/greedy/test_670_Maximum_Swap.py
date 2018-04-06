"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = map(int, str(num))
        l2 = sorted(l, reverse=1)
        candi = None
        for i in range(len(l)):
            if l[i] != l2[i]:
                candi = l2[i]
                break
        if candi:
            k = len(l) - 1 - l[::-1].index(candi)
            l[i], l[k] = l[k], l[i]
        return int(''.join(map(str, l)))

