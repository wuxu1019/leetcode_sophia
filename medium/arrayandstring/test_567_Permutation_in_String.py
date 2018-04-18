"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        ct1 = [0] * 26
        ct2 = [0] * 26
        for i in range(len(s1)):
            ct1[ord(s1[i]) - ord('a')] += 1
            ct2[ord(s2[i]) - ord('a')] += 1
        p, q = len(s1), 0
        while 1:
            if ct1 == ct2:
                return True
            if p < len(s2):
                ct2[ord(s2[p]) - ord('a')] += 1
                ct2[ord(s2[q]) - ord('a')] -= 1
                p, q = p + 1, q + 1
            else:
                break
        return False

if __name__ == '__main__':
    s = Solution()
    s1 = 'ab'
    s2 = 'jasdwebawq'
    rt1 = s.checkInclusion(s1, s2)
    s2 = 'asdrqwe'
    rt2 = s.checkInclusion(s1, s2)
    print rt1
    print rt2