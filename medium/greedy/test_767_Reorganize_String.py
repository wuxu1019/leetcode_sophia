"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

class Solution(object):
    def reorganizeString_count(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        ct = collections.Counter(S)
        ct_e = [(k, v) for k, v in ct.items()]
        ct_e.sort(key=lambda p:p[1], reverse=1)
        base = ct_e[0][1]
        if base > -int(-len(S)/2):
            return ""
        S = ""
        rt = ""
        for k, v in ct_e:
            S += k * v
        for i in range(base):
            rt += S[i]
            j = i + base
            while j < len(S):
                rt += S[j]
                j = j + base
        return rt

    def reorganizeString_greedy(self, S):
        """
        :type S: str
        :rtype: str
        """
        h = [(-S.count(i), i) for i in set(S)]
        heapq.heapify(h)
        if any(-c > (len(S) + 1) / 2 for c, v in h):
            return ""
        ans = ""
        while len(h) >= 2:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            ans += a[1] + b[1]
            if a[0] + 1 < 0:
                heapq.heappush(h, (a[0] + 1, a[1]))
            if b[0] + 1 < 0:
                heapq.heappush(h, (b[0] + 1, b[1]))
        if h:
            ans += heapq.heappop(h)[1]
        return ans