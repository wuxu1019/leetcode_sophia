"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""


class Solution(object):
    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = set()
        j = i = 0
        maxlth = 0
        while i < len(s) and j < len(s):
            if s[j] not in record:
                record.add(s[j])
                j += 1
                maxlth = max(maxlth, j - i)
            else:
                record.remove(s[i])
                i += 1
        return maxlth

    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = collections.Counter()
        i = 0
        maxlth = 0
        for j in range(len(s)):
            record[s[j]] += 1
            while 2 in record.values():
                record[s[i]] -= 1
                i += 1
            maxlth = max(maxlth, j - i + 1)
        return maxlth

    def lengthOfLongestSubstring_3(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in pos and i <= pos[s[j]]:
                i = pos[s[j]] + 1
            else:
                ans = max(ans, j - i + 1)
            pos[s[j]] = j
        return ans

    def lengthOfLongestSubstring_bitmap(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = [-1] * 256
        i = 0
        ans = 0
        for j in range(len(s)):
            p = ord(s[j])
            if pos[p] >= 0 and i <= pos[p]:
                i = pos[p] + 1
            else:
                ans = max(ans, j - i + 1)
            pos[p] = j
        return ans


