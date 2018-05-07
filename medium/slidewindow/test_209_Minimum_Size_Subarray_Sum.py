"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""


class Solution(object):
    def minSubArrayLen_bruteforce(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = float('INF')
        record = [nums[0]]
        for i in range(1, len(nums)):
            record.append(record[i-1] + nums[i])

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sm = record[j] - record[i] + nums[i]
                if sm >= s:
                    ans = min(ans, j - i + 1)
        return ans if ans != float('INF') else 0

    def minSubArrayLen_binarysearch(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = float('INF')
        record = [nums[0]]
        for i in range(1, len(nums)):
            record.append(record[i - 1] + nums[i])

        for i in range(0, len(nums)):
            if i == 0:
                to_find = s
            else:
                to_find = s + record[i - 1]
            j = bisect.bisect_left(record, to_find, i)
            if j < len(nums):
                ans = min(ans, j - i + 1)

        return ans if ans != float('INF') else 0

    def minSubArrayLen_onepass(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        sm = 0
        ans = float('INF')
        for i in range(len(nums)):
            sm += nums[i]
            while sm >= s:
                ans = min(ans, i - j + 1)
                sm -= nums[j]
                j += 1

        return ans if ans != float('INF') else 0
