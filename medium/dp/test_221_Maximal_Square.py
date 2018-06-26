"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution(object):
    def maximalSquare_bf(self, matrix):

    def maximalSquare_dp(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        dp = [int(v) for v in matrix[0]]
        dp_n = [0] * len(matrix[0])
        ans = max(dp)
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    dp_n[j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '0':
                        dp_n[j] = 0
                    else:
                        dp_n[j] = min(dp_n[j-1], dp[j], dp[j-1]) + 1
            ans = max(ans, max(dp_n))
            dp, dp_n = dp_n, dp
        return ans * ans