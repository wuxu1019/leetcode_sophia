


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candi1, candi2 = 0, 0
        count1, count2 = 0, 0
        for num in nums:
            if num == candi1:
                count1 += 1
            elif num == candi2:
                count2 += 1
            elif count1 == 0:
                candi1, count1 = num, 1
            elif count2 == 0:
                candi2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [i for i in set([candi1, candi2]) if nums.count(i) > len(nums) / 3]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 2, 3, 3, 3, 1]
    rt1 = s.majorityElement(nums)
    print rt1