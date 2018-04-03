"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
import collections

class Solution(object):
    def sortColors_twopass(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ct = collections.Counter(nums)
        j = 0
        for i in [0, 1, 2]:
            c = ct[i]
            while c:
                c -= 1
                nums[j] = i
                j += 1
        return nums

    def sortColors_onepass(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p1, p2 = 0, 0, len(nums) - 1
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p1 += 1
                p0 += 1
            elif nums[p1] == 1:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 1, 0, 0, 1, 0, 2]
    rt1 = s.sortColors_onepass(nums)
    print rt1
    rt2 = s.sortColors_twopass(nums)
    print rt2