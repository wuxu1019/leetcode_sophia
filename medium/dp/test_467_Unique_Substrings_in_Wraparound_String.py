"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

import collections


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0
        ans = 0
        record = collections.defaultdict(int)
        record[p[0]] = 1
        ct = 1
        for i in range(1, len(p)):
            diff = ord(p[i]) - ord(p[i - 1])
            if diff == 1 or diff == -25:
                ct += 1
            else:
                ct = 1
            record[p[i]] = max(record[p[i]], ct)
        return sum(record.values())


if __name__ == '__main__':
    s = Solution()
    strings = 'abcdrghajsmbcdef'
    rt = s.findSubstringInWraproundString(strings)
    print rt