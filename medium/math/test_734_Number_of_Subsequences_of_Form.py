"""
Given a string, count number of subsequences of the form a^i b^j c^ k, i.e., it consists of i a characters, followed by j b characters, followed by k c characters where i >= 1, j >=1 and k >= 1.

Note: Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.

Have you met this question in a real interview?
Example
Given s = abbc, return 3
Subsequences are abc, abc and abbc

Given s = abcabc, return 7
Subsequences are abc, abc, abbc, aabc, abcc, abc and abc
"""


class Solution:
    """
    @param source: the input string
    @return: the number of subsequences
    """

    def countSubsequences(self, source):
        # write your code here
        mp = {1: 'a', 2: 'b', 3: 'c'}

        def countSubsequencesHelper(src, key):
            if key not in mp:
                return 1
            if not src:
                return 0
            v = mp[key]
            ct, rt = 0, 0
            for n, c in enumerate(src):
                if c == v:
                    rt += (2 ** ct) * countSubsequencesHelper(src[n + 1:], key + 1)
                    ct += 1
            return rt

        return countSubsequencesHelper(source, 1)

