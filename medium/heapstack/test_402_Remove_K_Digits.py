"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return '0'

        for _ in range(k):
            i, j = 0, 0
            while j + 1 < len(num) and num[j + 1] >= num[j]:
                j += 1
            if num[i] > num[j]:
                num = num[i + 1:]
            else:
                num = num[:j] + num[j + 1:]

        num = num.lstrip('0')
        return '0' if not num else num

    def removeKdigits_stk_way(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stk = []
        i = 0
        for c in num:
            while stk and c < stk[-1] and k:
                stk.pop()
                k -= 1
            stk.append(c)

        if k:
            rt = stk[:-k]
        else:
            rt = stk[:]
        rt = ''.join(rt).lstrip('0')
        return rt if rt else '0'

