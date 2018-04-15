"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""
import collections
import bisect_sample

class Solution(object):
    def isSubsequence1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp = collections.defaultdict(list)
        last = -1
        for n, v in enumerate(t):
            mp[v].append(n)
        for c in s:
            if not c in mp or not mp[c]:
                return False
            while mp[c]:
                i = mp[c].pop(0)
                if i > last:
                    last = i
                    break
            if i != last:
                return False
        return True

    def isSubsequence2(self, s, t):
        mp = collections.defaultdict(list)
        last = -1
        for n, v in enumerate(t):
            mp[v].append(n)

        for c in s:
            if not c in mp:
                return False
            index = bisect_sample.bisect_sample(mp[c], last)
            if index == len(mp[c]):
                return False
            last = mp[c][index]
        return True

    def isSubsequence3(self, s, t):
        t = iter(t)
        return all(c in t for c in s)



if __name__ == '__main__':
    testcase = Solution()
    t = "abc"
    s = "bahgdcb"
    result = testcase.isSubsequence1(s, t)
    print result

    t = "qwe"
    s = "qe"
    result = testcase.isSubsequence1(s, t)
    print result

    t = "bahgdcb"
    s = "abc"
    result = testcase.isSubsequence2(s, t)
    print result

    t = "qwe"
    s = "qe"
    result = testcase.isSubsequence2(s, t)
    print result

    t = "bahgdcb"
    s = "abc"
    result = testcase.isSubsequence3(s, t)
    print result

    t = "qwe"
    s = "qe"
    result = testcase.isSubsequence3(s, t)
    print result