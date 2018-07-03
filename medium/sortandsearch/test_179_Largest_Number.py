"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        trans = map(str, nums)
        trans.sort(cmp=comp, reverse=True)
        rt = ''.join(trans)
        if rt.count('0') == len(rt):
            return '0'
        return rt
