"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
Credits:
Special thanks to @Stomach_ache for adding this problem and creating all test cases.


"""

class Solution(object):
    def largestDivisibleSubset_dp1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        record = {1:[]}
        for num in nums:
            candi = []
            for k, v in record.items():
                if num % k == 0:
                    candi.append(v + [num])
            record[num] = max(candi, key=len)
        return max(record.values(), key=len)


if __name__ == '__main__':
    s = Solution()
    num = [1,2,4,8,12,24, 28, 32, 36, 38, 40, 42, 48]
    rt1 = s.largestDivisibleSubset_dp1(num)
    print rt1