"""
A peak element is an element that is greater than its neighbors.

Given an input array, find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

class Solution(object):
    def findPeakElement_heap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        pos = {}
        for i in range(len(nums)/2-1, -1, -1):
            l = i*2 + 1
            r = i*2 + 2
            p = i
            if l < len(nums) and nums[p] < nums[l]:
                p = l
            if r < len(nums) and nums[p] < nums[r]:
                p = r
            if not nums[p] in pos:
                pos[nums[p]] = p
            if p != i:
                nums[i], nums[p] = nums[p], nums[i]
        return pos[nums[0]]


    def findPeakElemnt_bs(self, nums):

         l, r = 0, len(nums)-1
         while l < r:
             mid = (l + r) / 2
             if nums[mid] < nums[mid + 1]:
                 l = mid + 1
             else:
                 r = mid
         return l

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 6, 4]
    rt1 = s.findPeakElement_heap(nums)
    nums = [1, 2, 6, 4]
    rt2 = s.findPeakElemnt_bs(nums)

    print rt1
    print rt2