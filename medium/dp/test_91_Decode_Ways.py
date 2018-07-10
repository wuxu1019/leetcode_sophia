"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        ct = [0] * (len(s))
        ct[0] = 1

        for i in range(1, len(s)):
            calc = 0
            if s[i] == '0':
                if s[i - 1] not in '12':
                    return 0
                else:
                    calc += ct[i - 2] if i - 2 >= 0 else 1
            else:
                calc += ct[i - 1]
                if s[i - 1] != '0' and 1 <= int(s[i - 1:i + 1]) <= 26:
                    calc += ct[i - 2] if i - 2 >= 0 else 1
            ct[i] = calc
        return ct[-1]

