"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome_roundcompare(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, 0
        rt = ''

        while i < len(s) and j < len(s):
            sub = self.getSubPalindromeLenth(s, i, j)
            if len(sub) > len(rt):
                rt = sub
            if i == j:
                j += 1
            else:
                i += 1
        return rt

    def getSubPalindromeLenth(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i - 1, j + 1
        return s[i + 1:j]

    def longestPalindrome_dp(self, s):
        """
        :type s: str
        :rtype: str
        """
        lth = len(s)
        dp = [[False] * lth for _ in range(lth)]
        maxlth, rt = 0, ''
        for i in range(lth - 1, -1, -1):
            for j in range(i, lth):
                if s[i] == s[j] and ((j - i) < 2 or dp[i + 1][j - 1] == True):
                    dp[i][j] = True
                    dis = j - i + 1
                    if dis > maxlth:
                        rt = s[i:j + 1]
                        maxlth = dis

        return rt

