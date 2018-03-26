"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


"""

class Solution(object):
    def findMaxLength_bf(self, nums):
        rt = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                ct_1 = nums[i: j+1].count(0)
                ct_0 = nums[i: j+1].count(1)
                if ct_1 == ct_0:
                    rt = max(rt, ct_0+ct_1)
        return rt

    def findMaxLength_hashmap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = {0: -1}
        ct, rt = 0, 0
        for i, num in enumerate(nums):
            if num:
                ct += 1
            else:
                ct -= 1
            if ct not in record:
                record[ct] = i
            else:
                rt = max(rt, i-record[ct])
        return rt

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    rt1 = s.findMaxLength_hashmap(nums)
    print rt1

    rt2 = s.findMaxLength_bf(nums)
    print rt2