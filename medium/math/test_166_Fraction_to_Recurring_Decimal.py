"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        if numerator / denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator / denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator / denominator)
        res += "."
        numerator %= denominator
        i = len(res)
        table = {}
        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator / denominator)
            numerator %= denominator
            i += 1
        return res

