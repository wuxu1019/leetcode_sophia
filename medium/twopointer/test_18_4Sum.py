"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                t = target - nums[i] - nums[j]
                dic = set()
                for k in range(j+1, len(nums)):
                    diff = t - nums[k]
                    if diff in dic:
                        ans.add((nums[i], nums[j], diff, nums[k]))
                    else:
                        dic.add(nums[k])
        return [list(l) for l in ans]

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        t = target - nums[i] - nums[j]
                        a, b = j + 1, len(nums) - 1
                        while a < b:
                            s = nums[a] + nums[b]
                            if s == t:
                                ans.append([nums[i], nums[j], nums[a], nums[b]])
                                while a < b and nums[a] == nums[a + 1]:
                                    a += 1
                                while a < b and nums[b] == nums[b - 1]:
                                    b -= 1
                                a += 1
                                b -= 1
                            elif s < t:
                                a += 1
                            else:
                                b -= 1

        return ans