"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].

"""
import collections


class Solution(object):
    def deleteAndEarn_dp1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp, memo = {}, {}
        for num in nums:
            mp[num] = mp.get(num, 0) + num

        def helper(nums, s, mp):
            if s < 0:
                return 0
            if s == 0:
                return mp[nums[s]]
            if s in memo:
                return memo[s]
            if nums[s] != nums[s - 1] + 1:
                return mp[nums[s]] + helper(nums, s - 1, mp)
            s1 = mp[nums[s]] + helper(nums, s - 2, mp)
            s2 = helper(nums, s - 1, mp)
            s_max = max(s1, s2)
            memo[s] = s_max
            return s_max

        return helper(sorted(mp.keys()), len(mp) - 1, mp)

    def deleteAndEarn_dp2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
           """
        vals = collections.Counter(nums)
        no_use, use = 0, 0
        last = float('INF')
        for k in sorted(vals):
            if k == last + 1:
                no_use, use = max(no_use, use), no_use + k * vals[k]
            else:
                no_use, use = max(no_use, use), max(no_use, use) + k * vals[k]
            last = k
        return max(no_use, use)


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 3, 4, 4, 4, 5, 6, 6, 7]
    rt1 = s.deleteAndEarn_dp1(nums)
    print rt1
    rt2 = s.deleteAndEarn_dp2(nums)
    print rt2
