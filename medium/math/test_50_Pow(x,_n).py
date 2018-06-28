"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""


class Solution(object):
    def myPow_recursive(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            n = -n
            return self.myPow(1/x, n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        return self.myPow(x*x, n/2) * x

    def myPow_iter(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1/x

        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n = n >> 1
        return ans

    def myPow_bitmap(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        bitmap = bin(n)[2:]
        ans = 1
        for bit in bitmap[::-1]:
            if bit == '1':
                ans *= x
            x = x * x
        return ans
