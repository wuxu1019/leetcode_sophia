"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(height) - 1
        rt = 0
        while p2 > p1:
            rt = max(rt, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return rt

