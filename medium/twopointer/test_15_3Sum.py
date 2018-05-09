"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        i = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p, q = i + 1, len(nums) - 1
            while p < q:
                sm = nums[i] + nums[p] + nums[q]
                if sm == 0:
                    ans.append([nums[i], nums[p], nums[q]])
                    while p < q and nums[p] == nums[p + 1]:
                        p += 1
                    while p < q and nums[q] == nums[q - 1]:
                        q -= 1
                    p += 1
                    q -= 1
                elif sm > 0:
                    q -= 1
                else:
                    p += 1
        return ans

