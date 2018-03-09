"""

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).


"""


class Solution(object):
    def findMinArrowShots1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        p, ct = 0, 0
        points.sort(key = lambda x: x[1])
        while p < len(points):
            end = points[p][1]
            ct += 1
            p += 1
            while p < len(points):
                if points[p][0] <= end and points[p][1] >= end:
                    p += 1
                else:
                    break
        return ct

    def findMinArrowShots2(self, points):
        points = sorted(points, key=lambda x:x[1])
        res, end = 0, -float('INF')
        for p in points:
            if p[0] > end:
                res += 1
                end = p[1]
        return res

if __name__ == '__main__':
    s = Solution()
    input = [[10,16], [2,8], [1,6], [7,12]]
    res1 = s.findMinArrowShots1(input)
    res2 = s.findMinArrowShots2(input)

    print res1
    print res2