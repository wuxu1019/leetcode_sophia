"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299

"""


class Solution(object):
    def monotoneIncreasingDigits_dfs(self, N):
        """
        :type N: int
        :rtype: int
        """
        ln = [int(i) for i in str(N)]

        def monotoneIncreasingDigitsHelper(l):
            decrease = False
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    decrease = True
                    break
            if not decrease:
                return l
            else:
                return monotoneIncreasingDigitsHelper(l[:i] + [l[i] - 1] + [9] * (len(l) - 1 - i))

        return int(''.join([str(i) for i in monotoneIncreasingDigitsHelper(ln)]))

    def monotoneIncreasingDigits_greedy(self, N):
        digits = []
        A = map(int, str(N))
        for i in xrange(len(A)):
            s = digits[-1] if digits else 0
            for d in xrange(s, 10):
                if digits + [d] * (len(A) - i) > A:
                    digits.append(d - 1)
                    break
            else:
                digits.append(9)

        return int("".join(map(str, digits)))

if __name__ == '__main__':
    s = Solution()
    N = 1244283
    rt1 = s.monotoneIncreasingDigits_greedy(N)

    rt2 = s.monotoneIncreasingDigits_dfs(N)
    print rt1
    print rt2