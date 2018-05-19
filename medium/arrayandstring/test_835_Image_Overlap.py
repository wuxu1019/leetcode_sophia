"""
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1

"""

class Solution(object):
    def largestOverlap_trans(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        set_A, set_B = set(), set()
        R, C = len(A), len(A[0])
        ans = 0
        for i in range(R):
            for j in range(C):
                if A[i][j] == 1:
                    set_A.add((i, j))
                if B[i][j] == 1:
                    set_B.add((i, j))
        for i in range(-R+1, R):
            for j in range(-C+1, C):
                set_move = set()
                for a, b in set_A:
                    a = a + i
                    b = b + j
                    if 0 <= a < R and 0 <= b < C:
                        set_move.add((a, b))
                ans = max(len(set_move & set_B), ans)
        return ans

    def largestOverlap_count_delta(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        ct = collections.Counter()
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if v:
                    for i_b, row_b in enumerate(B):
                        for j_b, v_b in enumerate(row_b):
                            if v_b:
                                ct[(i - i_b, j - j_b)] += 1
        if ct:
            return max(ct.values())
        else:
            return 0