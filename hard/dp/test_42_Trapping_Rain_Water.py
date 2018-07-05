"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


class Solution(object):
    def trap_dp(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) <= 2:
            return 0
        ml1 = [height[0]]
        for h in height[1:]:
            ml1.append(max(ml1[-1], h))
        ml2 = [height[-1]]
        for h in height[:-1][::-1]:
            ml2 = [max(h, ml2[0])] + ml2

        rt = sum(min(ml1[i], ml2[i]) - height[i] for i in range(len(height)))
        return rt

    def trap_two_pointer(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans = 0
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans