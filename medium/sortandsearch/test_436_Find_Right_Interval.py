"""
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution1(object):
    def binary_search(self, target, s, e, l):

        while s <= e:
            mid = s + (e - s) / 2
            if l[mid][0].start == target[0].end:
                return mid
            elif l[mid][0].start > target[0].end:
                e = mid - 1
            else:
                s = mid + 1
        return s

    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        lth = len(intervals)
        if lth == 0:
            return []
        rt = []
        l = []
        for i in range(lth):
            l.append((intervals[i], i))
        l.sort(key=lambda i: (i[0].start, i[0].end))

        for i in range(0, lth - 1):
            insert = self.binary_search(l[i], i, lth - 1, l)
            if insert < lth:
                rt.append((l[i][1], l[insert][1]))
            else:
                rt.append((l[i][1], -1))

        rt.append((l[-1][1], -1))
        return [i[1] for i in sorted(rt)]

class Solution2(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        lth = len(intervals)
        if lth <= 0:
            return []
        l, rt = [], []
        for i, v in enumerate(intervals):
            l.append((v.start, i))
        l.sort()
        for interval in intervals:
            index = bisect.bisect(l, (interval.end, ))
            if index < lth:
                rt.append(l[index][1])
            else:
                rt.append(-1)
        return rt