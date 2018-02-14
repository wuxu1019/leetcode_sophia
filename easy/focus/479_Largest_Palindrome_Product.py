"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].


"""

ass Solution(object):
    def largestPalindrome(self, n):
        if n==1:
            return 9
        upper = 10 ** n-1
        lower = upper/10
        maxProduct = upper ** 2
        firstHalf = maxProduct/(10 ** n)
        
        while 1:
            candi = int(str(firstHalf)[::-1]) + firstHalf * (10 ** n)
            firstHalf -= 1
            if candi > maxProduct:
                continue
            for i in xrange(upper, lower, -1):
                if candi/i > upper:
                    continue
                if candi % i == 0:
                    return candi% 1337
        
