"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""



class Solution(object):
    def findLength_bf(self, A, B):
        ctb = {}
        rt = 0
        for i, v in enumerate(B):
            ctb[v] = ctb.get(v, []) + [i]

        for i, v in enumerate(A):
            if v in ctb:
                for j in ctb[v]:
                    ct = 0
                    while i < len(A) and j < len(B) and A[i] == B[j]:
                        ct += 1
                        i, j = i+1, j+1
                    rt = max(rt, ct)
        return rt

    def findLength_dp(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0] * len(A) for _ in range(len(B))]

        for i in range(len(B)):
            for j in range(len(A)):
                if B[i] == A[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1

        return max(max(row) for row in dp)

if __name__ == '__main__':
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    s = Solution()
    rt1 = s.findLength_dp(A, B)
    rt2 = s.findLength_bf(A, B)
    print rt2
    print rt1