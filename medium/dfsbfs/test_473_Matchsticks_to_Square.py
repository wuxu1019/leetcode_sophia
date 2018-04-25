"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

"""

import collections
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False
        arv, res = divmod(sum(nums), 4)
        if res:
            return False
        return self.dfs([arv] * 4, sorted(nums, reverse=1), 0)

    def dfs(self, l, nums, p):
        if l == [0] * 4 and p == len(nums):
            return True
        ct = collections.defaultdict(list)
        for i, v in enumerate(l):
            ct[v].append(i)
        for k, v in ct.items():
            if k >= nums[p]:
                l[v[0]] -= nums[p]
                if self.dfs(l, nums, p + 1):
                    return True
                l[v[0]] += nums[p]
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 2, 2]
    rt = s.makesquare(nums)
    print rt