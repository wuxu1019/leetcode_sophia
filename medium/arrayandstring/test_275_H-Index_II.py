"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Seen this question in a real interview before?
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        lth = len(citations)
        lo, hi = 0, lth - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if citations[mid] < lth - mid:
                lo = mid + 1
            elif citations[mid] > lth - mid:
                hi = mid - 1
            else:
                return citations[mid]
        return lth - lo