"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


"""

class Solution(object):
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for c in nums:
            a, b = (~a&b&c)|(a&~b&~c), (~a&~b&c)|(~a&b&~c)
        return b

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 2, 3, 2, 3]
    rt1 = s.singleNumber_1(nums)
    print rt1