"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

"""


class Solution(object):
    def validSquare_1(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        p = sorted([p1, p2, p3, p4], key=lambda i: (i[0], i[1]))
        d1 = dist(p[0], p[1])
        d2 = dist(p[0], p[2])
        d3 = dist(p[3], p[1])
        d4 = dist(p[3], p[2])
        d5 = dist(p[0], p[3])
        if d1 and d1 == d2 and d3 == d4 and d1 == d4 and d5 == d1 + d3:
            return True
        return False

    def validSquare_2(self, p1, p2, p3, p4):
        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        dist_l = {}
        p_l = [p1, p2, p3, p4]
        for i in range(len(p_l) - 1):
            for j in range(i + 1, len(p_l)):
                d = dist(p_l[i], p_l[j])
                dist_l[d] = dist_l.get(d, 0) + 1
        return len(dist_l.keys()) == 2 and 2 in dist_l.values() and 4 in dist_l.values()

if __name__ == '__main__':
    s = Solution()
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    rt1 = s.validSquare_1(p1, p2, p3, p4)
    rt2 = s.validSquare_2(p1, p2, p3, p4)
    print rt1
    print rt2
