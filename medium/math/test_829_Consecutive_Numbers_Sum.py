"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.


"""
"""
basic idea is that if it can divide m and N/m is and odd number, than it can combine a consecutive 
of N/m number summary

example:
12 can divided by 1, 2, 3, 4, 6, 12
12/1 = 12 is not odd
12/2 = 6 is not odd
12/3 = 4 is not odd
12/4 = 3 is odd, means 3, 4, 5
12/6 = 2 is not odd
12/12 = 1 is odd, means 12

so result is 2
to be simple, only need to count sqrt(N)
"""

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        rt = 0
        for i in range(1, int(math.sqrt(N) + 1)):
            if N % i == 0:
                a, b = i, N / i
                if a % 2 == 1:
                    rt += 1
                if b != a and b % 2 == 1:
                    rt += 1
        return rt
