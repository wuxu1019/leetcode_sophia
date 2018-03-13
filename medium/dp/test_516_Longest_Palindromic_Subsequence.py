"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

"""


class Solution(object):
    def longestPalindromeSubseq_1(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [0 for j in xrange(n)]
        dp[n - 1] = 1

        for i in xrange(n - 1, -1, -1):  # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in xrange(i + 1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]
                else:
                    newdp[j] = max(dp[j], newdp[j - 1])
            dp = newdp

        return dp[n - 1]

    def longestPalindromeSubseq_2(self, s):
        dp = [0] * len(s)

        for i in range(len(s) - 1, -1, -1):
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    newdp[j] = dp[j - 1] + 2
                else:
                    newdp[j] = max(newdp[j - 1], dp[j])
            dp = newdp
        return dp[-1]

    def longestPalindromeSubseq_3(self, s):
        d = {}
        def helper(s):
            if s in d:
                return s[d]
            max_lth = 0
            for c in set(s):
                l = s.find(c)
                r = s.rfind(c)
                max_lth = max(max_lth, 1 if l==r else 2+helper(s[l+1:r]))
            d[s] = max_lth
            return max_lth
        return helper(s)

if __name__ == '__main__':
    s = Solution()
    l = 'bbbab'
    rt1 = s.longestPalindromeSubseq_1(l)
    print rt1

    rt2 = s.longestPalindromeSubseq_2(l)
    print rt2

    rt3 = s.longestPalindromeSubseq_3(l)
    print rt3