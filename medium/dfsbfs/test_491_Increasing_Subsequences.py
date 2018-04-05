"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""


class Solution(object):
    def findSubsequences_backtrack1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = []
        for i in range(1, len(nums)):
            news = []
            for item in rt:
                if nums[i] >= item[-1]:
                    news.append(item + [nums[i]])
            for j in range(0, i):
                if nums[i] >= nums[j]:
                    news.append([nums[j], nums[i]])
            rt.extend(news)

        rt = set([tuple(i) for i in rt])
        return [list(i) for i in rt]

    def findSubsequences_backtrack2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = []
        for i in range(len(nums)):
            lth = len(rt)
            p = 0
            while p < lth:
                if rt[p][-1] <= nums[i]:
                    rt.append(rt[p] + [nums[i]])
                p += 1
            rt.append([nums[i]])

        rt = set([tuple(i) for i in rt])
        return [list(i) for i in rt if len(i) > 1]


if  __name__ == '__main__':
    s = Solution()
    nums = [2, 4, 1, 3, 6, 4]
    rt1 = s.findSubsequences_backtrack1(nums)
    rt2 = s.findSubsequences_backtrack2(nums)

    print rt1
    print rt2
