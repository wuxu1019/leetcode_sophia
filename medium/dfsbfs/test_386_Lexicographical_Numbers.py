"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


"""

class Solution(object):
    def lexicalOrder_dfs(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rt = []
        def helper(base, left, n):
            if left < 0:
                return
            if base and base <= n:
                rt.append(base)
            start = 1 if not base else 0
            for i in range(start, 10):
                next = base*10 + i
                helper(next, left-1, n)
        helper(0, len(str(n)), n)
        return rt

    def lexicalOrder_math(self, n):
        rt = []
        curr = 1
        for _ in range(1, n + 1):
            rt.append(curr)
            if 10 * curr <= n:
                curr = curr * 10
            elif curr % 10 != 9 and curr + 1 <= n:
                curr = curr + 1
            else:
                while (curr / 10) % 10 == 9:
                    curr = curr / 10
                curr = curr / 10 + 1
        return rt

    def lexicalOrder_morespace(self, n):
        withkeys = []
        RANGE = 1000000
        for i in xrange(n):
            key = i
            while key < RANGE:
                key = key * 10
            withkeys.append(key * RANGE + i)
        withkeys.sort()
        return [i%RANGE for i in withkeys]

if __name__ == '__main__':
    s = Solution()
    rt1 = s.lexicalOrder_math(123)
    print rt1

    rt2 = s.lexicalOrder_math(123)
    print rt2