"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

class Solution(object):
    def characterReplacement_slidewindow1(self, st, k):
       record = [0] * 26
       s, e, rt = 0, 0, 0

       while e < len(st):
           record[ord(st[e]) - ord('a')] += 1
           while e-s+1 - max(record) > k:
               record[ord(st[s]) - ord('a')] -= 1
               s += 1
           if rt < e-s+1:
               rt = e-s+1
           e += 1
       return rt

    def characterReplacement_slidewindow2(self, st, k):
        record = [0]*26
        s, e= 0, 0
        while e < len(st):
            record[ord(st[e]) - ord('a')] += 1
            if e-s+1 - max(record) > k:
                record[ord(st[s]) - ord('a')] -= 1
                s += 1
            e += 1
        return e-s


if __name__ == '__main__':
    s = Solution()
    strings = 'abbabbabababb'
    k = 3
    rt1 = s.characterReplacement_slidewindow1(strings, k)
    print rt1

    rt2 = s.characterReplacement_slidewindow2(strings, k)
    print rt2






