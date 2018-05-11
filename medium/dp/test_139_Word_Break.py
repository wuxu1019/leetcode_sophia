"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution(object):
    def wordBreak_dfs(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        wordDict = set(wordDict)
        self.memo = {}
        return self.dfs(s, 0, len(s), wordDict)

    def dfs(self, s, i, j, wordDict):
        if i == j:
            return True
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        ans = False
        for p in range(i, j):
            sub = s[i:p + 1]
            if sub in wordDict:
                if self.dfs(s, p + 1, j, wordDict):
                    ans = True
                    break
        self.memo[(i, j)] = ans
        return ans

    def wordBreak_dp(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        mark = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                if s[i - len(w) + 1:i + 1] == w and (i - len(w) == -1 or mark[i - len(w)] == True):
                    mark[i] = True
        return mark[-1]


if __name__ == '__main__':
    s = Solution()
    strings = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    rt1 = s.wordBreak_dfs(strings, wordDict)
    rt2 = s.wordBreak_dp(strings, wordDict)

    print rt1
    print rt2



