"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


class Solution(object):
    def subsets_dfs1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]
        rt = []

        def helper(base, nums, i):
            if i == len(nums) - 1:
                rt.extend([base, base + [nums[i]]])
            else:
                helper(base + [nums[i]], nums, i + 1)
                helper(base, nums, i + 1)

        helper([], nums, 0)
        return rt

    def subsets_dfs2(self, nums):
        ret = []

        def helper(temp, nums, s, e):
            ret.append(temp)
            for i in range(s, e):
                helper(temp+[nums[i]], nums, i+1, e)
        helper([], nums, 0, len(nums))
        return ret

    def subsets_bitmap(self, nums):
        rt = []
        for i in xrange(1 << len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if (1 << j)&i:
                    tmp.append(nums[j])
            rt.append(tmp)
        return rt

    def subsets_iterative(self, nums):
        rt = [[]]

        for num in nums:
            rt += [i + [num] for i in rt]
        return rt


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    r1 = s.subsets_dfs1(nums)
    r2 = s.subsets_dfs2(nums)
    r3 = s.subsets_bitmap(nums)
    r4 = s.subsets_iterative(nums)
    print r1
    print r2
    print r3
    print r4

