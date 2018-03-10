"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution(object):
    def findTargetSumWays_dp1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memo = {(len(nums), 0): 1}
        def helper(nums, s, target):
            if (s, target) in memo:
                return memo[(s, target)]
            if s == len(nums):
                return 0
            ct = helper(nums, s+1, target+nums[s])+helper(nums, s+1, target-nums[s])
            memo[(s, target)] = ct
            return ct
        return helper(nums, 0, S)

    def findTargetSumWays_dp2(self, nums, S):
        record = {0:1}
        for num in nums:
            record2 = {}
            for i in record:
                record2[i+num] = record2.get(i+num, 0)+record[i]
                record2[i-num] = record2.get(i-num, 0)+record[i]
            record = record2
        return record.get(S, 0)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2,  2, 4, 1, 2, 4]
    target = 0
    rt1 = s.findTargetSumWays_dp1(nums, target)
    rt2 = s.findTargetSumWays_dp2(nums, target)
    print rt1
    print rt2