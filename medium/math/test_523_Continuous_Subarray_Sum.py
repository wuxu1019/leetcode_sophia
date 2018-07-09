"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""


class Solution(object):
    def checkSubarraySum_nk(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True if any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1)) else False

        for num in nums:
            ct2 = set()
            for base in ct1:
                ct2.add((base + num) % k)
            if 0 in ct2:
                return True
            ct1 = ct2
            ct1.add(num)
        return False


    def checkSubarraySum_n(self, nums, k):

        if k == 0:
            return True if any(nums[i] == nums[i+1] == 0 for i in range(len(nums)-1)) else False

        pos = {0: -1}
        calc = 0
        for n, num in enumerate(nums):
            calc += num
            calc_mod = calc % k

            if calc_mod in pos and n - pos[calc_mod] > 1:
                return True
            elif calc_mod not in pos:
                pos[calc_mod] = n
        return False
