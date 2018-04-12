"""
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)

"""

class Solution(object):
    def orderOfLargestPlusSign_bf(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        M = -(-N/2)
        for m in range(M, 0, -1):
            for x in range(m-1, N-m+1):
                for y in range(m-1, N-m+1):
                    found = True
                    for a in range(-(m-1), m):
                        if [x+a, y] in mines:
                            found = False
                            break
                        if [x, y+a] in mines:
                            found = False
                            break
                    if found:
                        return m
        return 0

    def orderOfLargestPlusSign_dp(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        dp = [[N] * N for _ in range(N)]

        for i, j in mines:
            dp[i][j] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if dp[i][j] != 0 else 0
                dp[i][j] = min(l, dp[i][j])

                r = r + 1 if dp[i][k] != 0 else 0
                dp[i][k] = min(r, dp[i][k])

                u = u + 1 if dp[j][i] != 0 else 0
                dp[j][i] = min(u, dp[j][i])

                d = d + 1 if dp[k][i] != 0 else 0
                dp[k][i] = min(d, dp[k][i])

        rt = 0
        for i in range(N):
            for j in range(N):
                rt = max(rt, dp[i][j])
        return rt

if __name__ == '__main__':
    s = Solution()
    N = 5
    mines = [[4, 2]]
    rt1 = s.orderOfLargestPlusSign_dp(N, mines)
    print rt1