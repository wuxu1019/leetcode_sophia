"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


class Solution(object):
    def find132pattern_brute_force_optimize(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ai = float('INF')
        for j in range(len(nums) - 1):
            ai = min(ai, nums[j])
            for k in range(j + 1, len(nums)):
                if nums[k] > ai and nums[k] < nums[j]:
                    return True
        return False

    def find132pattern_record_intervals(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        intervals = []
        s = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if s < i - 1:
                    intervals.append([s, i - 1])
                s = i
            for a, b in intervals:
                if nums[i] > nums[a] and nums[i] < nums[b]:
                    return True
        return False

    def find132pattern_nlogn(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False
        left = [nums[0]]
        for num in nums[1:]:
            left.append(min(left[-1], num))
        q = []
        right = [None] * len(nums)
        for i, num in enumerate(nums[::-1]):
            heapq.heappush(q, num)
            # print q
            while q and q[0] <= left[len(nums) - i - 1]:
                heapq.heappop(q)
            # print q
            # print '  '
            if q:
                right[len(nums) - i - 1] = q[0]
        # print left
        # print right
        for i, num in enumerate(nums):
            if right and left[i] < right[i] < num:
                return True
        return False

    def find132pattern_Stack(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        mini = [nums[0]]
        for num in nums[1:]:
            mini.append(min(mini[-1], num))

        stk = []
        for i in list(range(len(nums) - 1, -1, -1)):
            if nums[i] > mini[i]:
                while stk and stk[-1] <= mini[i]:
                    stk.pop()
                if stk and stk[-1] < nums[i]:
                    return True
                stk.append(nums[i])
        return False

