"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution(object):
    def wiggleSort_three_step(self, nums):
        """
        1. find the median num of nums
        2. three partition sort [< median, == median, > median]
        3. put the data back
        """

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        median = self.findKthLasgest(nums, (len(nums) + 1) / 2)
        i, j = 0, 0
        n = len(nums) - 1
        while j <= n:
            if nums[j] < median:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[j] > median:
                nums[n], nums[j] = nums[j], nums[n]
                n -= 1
            else:
                j += 1
        k = (len(nums) + 1) / 2
        nums[0:len(nums):2], nums[1:len(nums):2] = nums[:k][::-1], nums[k:][::-1]

    def findKthLasgest(self, A, k):
        def helper(s, e):
            pilot = A[s]
            p, q = s + 1, e
            while p <= q:
                if A[p] > pilot:
                    p += 1
                else:
                    A[p], A[q] = A[q], A[p]
                    q -= 1
            A[s], A[q] = A[q], A[s]

            if q == k:
                return pilot
            elif q > k:
                return helper(s, q - 1)
            else:
                return helper(q + 1, e)

        return helper(0, len(A) - 1)

    def wiggleSort_nlogn_sortway(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        k = (len(nums) + 1) / 2
        nums[0:len(nums):2], nums[1:len(nums):2] = nums[:k][::-1], nums[k:][::-1]
