"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""
import bisect_sample

class Solution(object):
    def lengthOfLIS_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            m = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    m = max(dp[j], m)
            dp[i] = m + 1
        return max(dp)

    def lengthOfLIS_bs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        record = []
        for num in nums:
            p = bisect_sample.bisect_left(record, num)
            if p >= len(record):
                record.append(num)
            else:
                record[p] = num
        return len(record)

if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    rt1 = s.lengthOfLIS_bs(nums)
    rt2 = s.lengthOfLIS_dp(nums)
    print rt1
    print rt2

    nums = [2, 2, 2]
    rt1 = s.lengthOfLIS_bs(nums)
    rt2 = s.lengthOfLIS_dp(nums)
    print rt1
    print rt2