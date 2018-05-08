"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        start = 0
        for p, group in itertools.groupby([n - v for n, v in enumerate(nums)]):
            interval = len(list(group))
            end = start + interval
            if interval == 1:
                ans.append(str(nums[start]))
            else:
                ans.append("{}->{}".format(nums[start], nums[end - 1]))
            start = end
        return ans

