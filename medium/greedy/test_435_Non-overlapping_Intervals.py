"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""


class Solution(object):
    def eraseOverlapIntervals_mine(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        ct = 0
        intervals.sort(key = lambda i :(i.start, i.end))
        p1 = intervals.pop(0)
        while intervals:
            p2 = intervals.pop(0)
            if p2.start >= p1.end:
                p1 = p2
                continue
            if p1.end >= p2.end:
                p1 = p2
            ct += 1
        return ct

    def eraseOverlapIntervals_greedy(self, intervals):
        intervals.sort(key = lambda x: x.start)
        ct = 0
        p1 = intervals[0].end
        for i in intervals[1:]:
            if i.start < p1:
                ct += 1
                p1 = min(i.end, p1)
            else:
                p1 = i.end
        return ct