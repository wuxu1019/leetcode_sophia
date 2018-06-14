"""
Description
Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Have you met this question in a real interview?
Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = bDefinition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        dis = []
        for p in points:
            d = (p.x - origin.x) ** 2 + (p.y - origin.y) ** 2
            dis.append([d, p.x, p.y])
        ans = []
        import heapq
        heapq.heapify(dis)
        for i in range(min(k, len(points))):
            d, x, y = heapq.heappop(dis)
            ans.append(Point(x, y))
        return ans
