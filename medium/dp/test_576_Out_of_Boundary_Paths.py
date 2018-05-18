"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].

"""


class Solution(object):

    def findPaths_dfs(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.MOD = 1000000007
        self.record = [[[None] * n for p in range(m)] for q in range(N)]
        return self.dfs(m, n, N - 1, i, j)

    def dfs(self, m, n, k, i, j):
        if i < 0 or i == m or j < 0 or j == n:
            return 1
        if k < 0:
            return 0
        if self.record[k][i][j]:
            return self.record[k][i][j]
        ct = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ct += self.dfs(m, n, k - 1, i + dx, j + dy) % self.MOD
        ct = ct % self.MOD
        self.record[k][i][j] = ct
        return ct

    def findPaths_dp(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 1000000007
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        ans = 0
        for time in range(N):
            dp_n = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= nx < m and 0 <= ny < n:
                            dp_n[nx][ny] += dp[i][j]
                            dp_n[nx][ny] %= MOD
                        else:
                            ans += dp[i][j]
                            ans %= MOD
            dp = dp_n
        return ans
