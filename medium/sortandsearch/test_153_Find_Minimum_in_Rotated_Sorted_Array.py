"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while hi - lo > 1:
            mid = lo + (hi - lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid
            elif nums[mid] < nums[lo]:
                hi = mid
            elif nums[mid] > nums[lo] and nums[mid] < nums[hi]:
                return nums[lo]
        return min(nums[lo], nums[hi])

    def findMin_bs(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) / 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    rt1 = s.findMin(nums)
    print rt1

    rt2 = s.findMin_bs(nums)
    print rt2