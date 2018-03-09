"""

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

"""


class Solution(object):
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return len(word1) + len(word2) - 2 * dp[-1][-1]

    def minDistance2(self, word1, word2):
        dp = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def minDistance3(self, word1, word2):

        def lcs(w1, w2, l1, l2):
            if l1 == 0 or l2 == 0:
                return 0
            if w1[l1-1] == w2[l2-1]:
                return 1+lcs(w1, w2, l1-1, l2-1)
            else:
                return max(lcs(w1, w2, l1-1, l2), lcs(w1, w2, l1, l2-1))

        return len(word2) + len(word1) - 2*lcs(word1, word2, len(word1), len(word2))


if  __name__ == '__main__':
    s = Solution()
    s1 = 'abcdsq'
    s2 = 'bdwdao'
    moves1 = s.minDistance1(s1, s2)
    print moves1

    moves2 = s.minDistance2(s1, s2)
    print moves2

    moves3 = s.minDistance3(s1, s2)
    print moves3