"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition_dfs_dp(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        palinpair = self.getPalinPair(s)
        rt = []
        self.dfs(0, len(s), palinpair, [], rt, s)
        return rt

    def getPalinPair(self, l):
        pair = collections.defaultdict(list)
        for i in range(len(l)):
            for e in [i, i+ 1]:
                s = i
                while s >= 0 and e < len(l) and l[s] == l[e]:
                    pair[s].append(e)
                    s -= 1
                    e += 1
        return pair

    def dfs(self, s, e, mp, base, rt, l):
        if s >= e:
            rt.append(base)
            return
        for pos in mp[s]:
            self.dfs(pos + 1, e, mp, base + [l[s:pos + 1]], rt, l)

    def partition_dfs(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.rt = []

        def dfs(base, l):
            if not l:
                self.rt.append(base)
                return
            for i in range(1, len(l) + 1):
                if l[:i] == l[:i][::-1]:
                    dfs(base + [l[:i]], l[i:])

        dfs([], s)
        return self.rt