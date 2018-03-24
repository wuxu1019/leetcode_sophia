"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""


class Solution(object):

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = 0
        if len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            lo = 0
            hi = i - 1
            while lo < hi:
                if nums[lo] + nums[hi] > nums[i]:
                    ct += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return ct

if __name__ == '__main__':
    s = Solution()
    nums = [2,2,3,4]
    rt = s.triangleNumber(nums)
    print rt