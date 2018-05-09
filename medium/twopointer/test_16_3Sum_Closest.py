"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

class Solution(object):
    def threeSumClosest_twopointer(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            lo, hi = i + 1, len(nums)-1
            while lo < hi:
                sm = nums[i] + nums[lo] + nums[hi]
                if sm == target:
                    return target
                if abs(sm - target) < abs(ans - target):
                    ans = sm
                if sm > target:
                    hi -= 1
                else:
                    lo += 1
        return ans

