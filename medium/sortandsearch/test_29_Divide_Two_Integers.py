"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

"""


class Solution(object):
    def divide_1(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        def limit(d):
            MAX = 2 ** 31 - 1
            MIN = - 2 ** 31
            if d > MAX:
                return MAX
            elif d < MIN:
                return MIN
            return d

        if dividend == 0:
            return 0

        sign_dividend = -1 if dividend < 0 else 1
        sign_divisor = -1 if divisor < 0 else 1

        sign = 1 if sign_dividend * sign_divisor == 1 else -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            temp = divisor
            ct = 1
            while temp <= dividend:
                temp = temp << 1
                ct = ct << 1
            dividend -= temp >> 1
            result += ct >> 1
        result = result if sign > 0 else -result
        return limit(result)

    def divide_2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = ((dividend > 0) != (divisor > 0))
        dividend = left = abs(dividend)
        divisor = div = abs(divisor)
        time = 1
        res = 0
        while left >= divisor:
            left -= div
            res += time
            div += div
            time += time
            if left < div:
                div = divisor
                time = 1
        if neg:
            return max(-2 ** 31, -res)
        else:
            return min(2 ** 31 - 1, res)