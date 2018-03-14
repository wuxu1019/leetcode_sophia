"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

class Solution(object):
    def lastRemaining_pints(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        left = 1
        rem = n
        step = 1
        while s != e:
            if left > 0:
                if rem % 2 != 0:
                    e = e - step
                s = s + step
            else:
                if rem % 2 != 0:
                    s = s + step
                e = e - step
            step = step *2
            rem = rem/2
            left = -left
        return s

    def lastRemaning_math(self, n):
        if n == 2 or n == 3:
            return 2
        if n == 1:
            return 1
        base = 4*self.lastRemaning_math(n/4)
        if n%4 == 0 or n%4 == 1:
            return base-2
        else:
            return base



if __name__ == '__main__':
    s = Solution()
    rt1 = s.lastRemaining_pints(9)
    rt2 = s.lastRemaning_math(9)

    print rt1
    print rt2