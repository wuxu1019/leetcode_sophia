"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""


class Solution(object):
    def searchRange_onepass(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        cs, ce = -1, -1
        while i <= j:
            mid_init = i + (j - i) / 2
            if nums[mid_init] == target:
                cs, ce = i, j
                break
            elif nums[mid_init] < target:
                i = mid_init + 1
            else:
                j = mid_init - 1
        if cs >= 0:
            i, j = cs, mid_init
            while i < j:
                mid = i + (j - i) / 2
                if nums[mid] == target:
                    j = mid
                else:
                    i = mid + 1
            cs = i
            i, j = mid_init, ce
            while i < j:
                mid = i + (j - i) / 2
                if nums[mid] == target:
                    i = mid + 1
                else:
                    j = mid
            if nums[i] == target:
                ce = i
            else:
                ce = i - 1
        return [cs, ce]

    def searchRange_twopass(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        leftmost = self.binarySearchExtention(nums, target, True)
        if leftmost >= len(nums) or nums[leftmost] != target:
            return [-1, -1]
        else:
            rightmost = self.binarySearchExtention(nums, target, False)
            return [leftmost, rightmost - 1]

    def binarySearchExtention(self, nums, target, leftmost):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) / 2
            if nums[mid] > target or (leftmost and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1
        return lo



