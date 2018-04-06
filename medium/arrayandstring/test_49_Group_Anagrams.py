"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

"""
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = collections.defaultdict(list)
        for i, s in enumerate(strs):
            bitstr = self.getbit(s)
            if bitstr in mp:
                mp[bitstr].append(s)
            else:
                mp[bitstr] = [s]
        return mp.values()

    def getbit(self, s):
        rt = [0] * 26
        for c in s:
            rt[ord(c) - ord('a')] += 1
        return ''.join(map(str, rt))


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    rt1 = s.groupAnagrams(strs)
    print rt1
