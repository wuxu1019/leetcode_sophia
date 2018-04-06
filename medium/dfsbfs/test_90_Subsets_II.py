"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

import collections


class Solution(object):
    def subsetsWithDup_dfs1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = []
        ct = collections.Counter(nums)

        def helper(l, i, base):
            if i == len(l):
                rt.append(base)
                return
            k, times = l[i]
            for t in range(times + 1):
                helper(l, i + 1, base + [k] * t)

        helper(ct.items(), 0, [])
        return rt

    def subsetsWithDup_itertator(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = [[]]
        nums.sort()
        l = 1
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(rt)
            for j in range(len(rt) - l, len(rt)):
                rt.append(rt[j] + [nums[i]])
        return rt

    def subsetsWithDup_dfs2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = []

        def dfs(nums, p, base):
            rt.append(base)
            for i in range(p, len(nums)):
                if i > p and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, i + 1, base + [nums[i]])

        nums.sort()
        dfs(nums, 0, [])
        return rt


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2]
    rt1 = s.subsetsWithDup_dfs1(nums)
    rt2 = s.subsetsWithDup_dfs2(nums)
    print rt1
    print rt2
