"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""


class Solution(object):
    def findDuplicate_cyclelinklist(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        f1 = 0
        f2 = slow
        while f1 != f2:
            f1 = nums[f1]
            f2 = nums[f2]
        return f1



if __name__ == '__main__':
    s = Solution()
    nums = [3, 3, 5, 1, 2, 4]
    rt = s.findDuplicate_cyclelinklist(nums)
    print rt
