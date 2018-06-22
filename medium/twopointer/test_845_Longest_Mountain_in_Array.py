"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = end = 0
        ans = 0

        while start < len(A):
            end = start
            while end + 1 < len(A) and A[end] < A[end + 1]:
                end += 1
            if end + 1 < len(A) and A[end] > A[end + 1]:
                while end + 1 < N and A[end] > A[end + 1]:
                    end += 1
                ans = max(ans, end - start + 1)
            start = max(end, start + 1)
        return ans

    def longestMountain_two_pass(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        up = [0] * len(A)
        down = [0] * len(A)

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1

        for i in range(0, len(A) - 1)[::-1]:
            if A[i] > A[i + 1]:
                down[i] = down[i + 1] + 1

        ans = 0
        for i in range(len(A)):
            if up[i] and down[i]:
                ans = max(up[i] + down[i] + 1, ans)
        return ans