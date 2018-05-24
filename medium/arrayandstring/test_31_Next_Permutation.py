"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)
        if not i:
            return
        for i in range(len(nums) - 1, -1, -1):
            if i == 0 or nums[i] > nums[i - 1]:
                break
        self.reverse(nums, i, len(nums) - 1)
        if i == 0:
            return
        j, i = i, i - 1
        while j < len(nums):
            if nums[j] <= nums[i]:
                j += 1
            else:
                break
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, l, i, j):
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1