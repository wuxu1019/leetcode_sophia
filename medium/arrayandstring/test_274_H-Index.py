
"""
e: If there are several possible values for h, the maximum one is taken as the h-index.
"""

class Solution(object):
    def hIndex_sort_nlogn(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=1)
        maxi = 0
        for i, v in enumerate(citations):
            maxi = max(min(i+1, v), maxi)
        return maxi

    def hIndex_countsort_n(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ct = [0] * (len(citations) + 1)
        for c in citations:
            if c >= len(citations):
                ct[-1] += 1
            else:
                ct[c] += 1

        num = 0
        for i in range(len(citations), -1, -1):
            num += ct[i]
            if num >= i:
                return i
        return 0

if __name__ == '__main__':
    s = Solution()
    citations = [3, 1, 0, 6, 8]
    rt1 = s.hIndex_countsort_n(citations)
    rt2 = s.hIndex_sort_nlogn(citations)
    print rt1
    print rt2