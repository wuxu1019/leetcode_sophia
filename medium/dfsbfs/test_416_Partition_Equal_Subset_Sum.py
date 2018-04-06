"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""


class Solution(object):
    def canPartition_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sm = sum(nums)
        if sm % 2:
            return False
        sm = sm / 2

        stk = {0}
        for num in nums:
            lth = len(stk)
            stkl = list(stk)
            p = 0
            while p < lth:
                if stkl[p] + num == sm:
                    return True
                stk.add(stkl[p] + num)
                p += 1
        return False

    def canPartition_recuisive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}

        def Helper(base, n):
            if base == sm:
                return True
            if base > sm:
                return False
            if n >= len(nums):
                return False
            if (base, n) in memo:
                return memo[(base, n)]
            rt = Helper(base + nums[n], n + 1) or Helper(base, n + 1)
            memo[(base, n)] = rt
            return rt

        sm = sum(nums)
        if sm % 2:
            return False
        sm = sm / 2
        return Helper(0, 0)