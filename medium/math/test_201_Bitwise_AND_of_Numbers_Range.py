"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example:

Input: [5,7]
Output: 4
Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
"""


class Solution(object):
    def rangeBitwiseAnd_1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = 0
        base = 1
        while base <= n:

            a, b = m & base, n & base
            if a == b:
                ans = ans + a
            else:
                ans = 0
            base = base << 1

        return ans

    def rangeBitwiseAnd_2(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i