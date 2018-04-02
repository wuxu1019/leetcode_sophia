"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ct = 0
        record = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1):
                record[j] += nums[i]
                if record[j] == k:
                    ct += 1
        return ct

    def subarraySum_2(self, nums, k):
        ct = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k:
                    ct += 1
        return ct

    def subarraySum_bitmap(self, nums, k):
        record = {0 : 1}
        s = 0
        ct = 0
        for num in nums:
            s += num
            diff = s - k
            if diff in record:
                ct += record[diff]
            record[num] = record.get(num, 0) + 1
        return ct



if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 3, 4, -2, -5, 4, 1]
    k = 7
    rt1 = s.subarraySum_1(nums, k)
    print rt1

    rt2 = s.subarraySum_2(nums, k)
    print rt2

    rt3 = s.subarraySum_bitmap(nums, k)
    print rt3

