"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:


"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res, rem = divmod(sum(nums), k)
        if rem:
            return False
        nums.sort(reverse=1)

        def dfs(k, sums, visit, target, inc):
            if k == 1:
                return True
            if sums == target:
                return dfs(k - 1, 0, visit, res, 0)
            for i in range(inc, len(visit)):
                if not visit[i] and sums + nums[i] <= target:
                    visit[i] = True
                    if dfs(k, sums + nums[i], visit, target, inc+1):
                        return True
                    visit[i] = False
            return False

        return dfs(k, 0, [False] * len(nums), res, 0)


if __name__ == '__main__':
    s = Solution()
    nums = [85,35,40,64,86,45,63,16,5364,110,5653,97,95]
    k = 7
    rt1 = s.canPartitionKSubsets(nums, k)
    print rt1