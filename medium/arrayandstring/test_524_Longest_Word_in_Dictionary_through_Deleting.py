"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

"""


class Solution(object):
    def findLongestWord_1(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        d.sort(key=len, reverse=True)

        for word in d:
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(word):
                if s[p1] != word[p2]:
                    p1 += 1
                else:
                    p1, p2 = p1 + 1, p2 + 1
            if p2 == len(word):
                return word
        return ""

    def findLongestWord_2(self, s, d):

        found = ""
        max_lth = -float('INF')


        for word in d:
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(word):
                if s[p1] != word[p2]:
                    p1 += 1
                else:
                    p1, p2 = p1 + 1, p2 + 1
            if p2 == len(word) and (p2 > max_lth or (p2  == max_lth and word < found)):
                found = word
                max_lth = p2

        return found

    def findLongestWord_3(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)

        return max(sorted(filter(isSubsequence, d)) + [''], key=len)


if __name__ == '__main__':
    s = Solution()
    st = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]

    rt1 = s.findLongestWord_1(st, d)
    print rt1

    rt2 = s.findLongestWord_2(st, d)
    print rt2

    rt3 = s.findLongestWord_3(st, d)
    print rt3
