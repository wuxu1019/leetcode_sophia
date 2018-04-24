"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].

"""
import collections
import bisect

class Solution(object):
    def numMatchingSubseq_bisect(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ct = collections.defaultdict(list)
        for i, c in enumerate(S):
            ct[c].append(i)
        return sum(self.findWord(word, 0, 0, ct) for word in words)

    def findWord(self, w, p, start, ct):
        if p == len(w):
            return True
        c = w[p]
        if c not in ct or start > ct[c][-1]:
            return False
        index = bisect.bisect_left(ct[c], start)
        if index == len(ct[c]):
            return False
        return self.findWord(w, p + 1, ct[c][index] + 1, ct)

    def numMatchingSubseq_iter(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))

        for c in S:
            for it in waiting.pop(c, []):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

if __name__ == '__main__':
    s = Solution()
    string = "abcde"
    words = ["a", "bb", "acd", "ace"]
    rt1 = s.numMatchingSubseq_bisect(string, words)
    rt2 = s.numMatchingSubseq_iter(string, words)
    print rt1
    print rt2