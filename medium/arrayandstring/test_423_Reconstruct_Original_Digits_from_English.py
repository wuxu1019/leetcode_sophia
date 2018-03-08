"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

"""
import copy
import collections

class Solution(object):
    def originalDigits1(self, s):
        """
        :type s: str
        :rtype: str
        """
        words_all = ['zero', 'one', 'two', 'three', 'four',
                     'five', 'six', 'seven', 'eight', 'nine']
        letters = {}
        for c in s:
            letters[c] = letters.get(c, 0) + 1

        def helper(l, words, last):
            if all([i == 0 for i in l.values()]) or not l:
                return ''
            rt = []
            for n, word in enumerate(words):
                includeword = True
                l_n = copy.deepcopy(l)
                for c in word:
                    if c not in l_n or l_n[c] <= 0:
                        includeword = False
                        break
                    else:
                        l_n[c] -= 1
                if includeword:
                    rt.append(str(n+last) + helper(l_n, words[n:], n+last))
            if rt:
                return max(rt, key=len)
            return ''

        return helper(letters, words_all, 0)

    def originalDigits2(self, s):
        """
        :type s: str
        :rtype: str
        """
        words_all = ['eroz', 'one', 'tow', 'treeh', 'four',
                     'five', 'six', 'seven', 'eight', 'nine']
        res = ''
        res += '0' * s.count('z')
        res += '1' * (s.count('o') - s.count('z') - s.count('w') -s.count('u'))
        res += '2' * s.count('w')
        res += '3' * (s.count('h') - s.count('g'))
        res += '4' * s.count('u')
        res += '5' * (s.count('f') - s.count('u'))
        res += '6' * s.count('x')
        res += '7' * (s.count('s') - s.count('x'))
        res += '8' * s.count('g')
        res += '9' * (s.count('i') - s.count('x') - s.count('g') -s.count('f') + s.count('u'))

        return res

    def orignialDigits3(self, s):
        d = collections.Counter(s)
        res = []
        for x in '0eroz 6six 7evens 5fiev 8eihtg 4ourf 3treeh 2tow 1neo 9nnei'.split():
            res.append(x[0] * d[x[-1]])
            for c in x:
                d[c] -= d[x[-1]]
        return ''.join(sorted(res))

if __name__ == '__main__':
    s = Solution()
    data = "seventwo"
    digitals = s.orignialDigits3(data)
    print digitals
