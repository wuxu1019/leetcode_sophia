"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        times = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                if times < 2:
                    i += 1
                    nums[i] = nums[j]
                    times += 1
            else:
                i += 1
                nums[i] = nums[j]
                times = 1
        return i+1

    def removeDuplicates_concise(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]
    rt1 = s.removeDuplicates(nums)
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]
    rt2 = s.removeDuplicates_concise(nums)

    print rt1
    print rt2
