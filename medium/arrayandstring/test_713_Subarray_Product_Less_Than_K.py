"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""


class Solution(object):
    def numSubarrayProductLessThanK_slidewindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        p = 1
        j = 0
        for i in range(len(nums)):
            p = p * nums[i]
            while j <= i and p >= k:
                p = p / nums[j]
                j += 1
            ans += i - j + 1
        return ans

    def numSubarrayProductLessThanK_bs(self, nums, k):

