"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199
"""
import itertools

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) <= 2:
            return False
        lth = len(num) - 1
        for x in range(1, lth):
            for y in range(1, lth - x + 1):
                if self.isValid(num, 0, x, x + y):
                    return True
        return False

    def isValid(self, num, s1, s2, s3):
        if s3 == len(num):
            return True
        if num[s1] == '0' and s2 - s1 > 1 or num[s2] == '0' and s3 - s2 > 1:
            return False
        a = int(num[s1:s2])
        b = int(num[s2:s3])
        add = a + b
        if str(add) == num[s3: s3 + len(str(add))]:
            if self.isValid(num, s2, s3, s3 + len(str(add))):
                return True
        return False

    def isAdditiveNumber_betterwriting(self, num):
        lth = len(num)
        for a, b in itertools.combinations(range(1, lth), 2):
            s1 = num[:a]
            s2 = num[a:b]

            if s1 != str(int(s1)):
                continue
            if s2 != str(int(s2)):
                continue

            while b < lth:
                s3 = str(int(s1) + int(s2))
                if not num.startswith(s3, b):
                    break
                s1, s2 = s2, s3
                b = b + len(s3)
            if b == lth:
                return True
        return False
