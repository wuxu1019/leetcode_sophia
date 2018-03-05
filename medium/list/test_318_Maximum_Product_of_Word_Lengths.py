"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

"""

import unittest

class Solution(object):
    def maxProduct(self, words):
        mp = {}

        for w in words:
            mask = 0
            for c in set(w):
                mask |= 1 << (ord(c) - ord('a'))
            mp[mask] = max(len(w), mp.get(mask, 0))

        product = [mp[x]*mp[y] for x in mp for y in mp if x&y == 0]

        return max(product) if product else 0



class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def testCase1(self):
        self.assertEqual(self.s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]), 4)

    def testCase2(self):
        self.assertEqual(self.s.maxProduct(["a", "aa", "aaa", "aaaa"]), 0)
