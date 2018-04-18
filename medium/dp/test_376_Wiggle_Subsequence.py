"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
"""

class Solution(object):
    def wiggleMaxLength_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)

    def wiggleMaxLength_greedy(self, nums):
        if len(nums) < 2:
            return len(nums)

        prediff = nums[1] - nums[0]
        ct = 1 if prediff == 0 else 2

        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0 and prediff <= 0 or diff < 0 and prediff >= 0:
                ct += 1
        return ct

if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 6, 6, 1, 1]
    rt1 = s.wiggleMaxLength_greedy(nums)
    rt2 = s.wiggleMaxLength_dp(nums)

    print rt1
    print rt2