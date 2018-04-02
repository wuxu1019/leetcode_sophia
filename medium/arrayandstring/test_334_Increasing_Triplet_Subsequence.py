"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.



Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
"""


class Solution(object):
    def increasingTriplet_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p1, p2 = float('INF'), float('INF')
        for num in nums:
            if num < p1:
                p1 = num
            elif num > p1 and num < p2:
                p2 = num
            elif num > p2:
                return True
        return False

    def increasingTriplet_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p1, p2 = float('INF'), float('INF')
        for num in nums:
            if num <= p1:
                p1 = num
            elif num <= p2:
                p2 = num
            else:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 0, 6]
    rt1 = s.increasingTriplet_1(nums)
    print rt1
    rt2 = s.increasingTriplet_2(nums)
    print rt2
