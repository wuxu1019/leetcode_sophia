



class Solution(object):
    def combine_dp(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rt = []
        def combineHelper(base, l, p, times):
            if times == 0:
                rt.append(base)
                return
            i = p
            while i < len(l):
                combineHelper(base+[l[i]], l, i+1, times-1)
                i += 1
        if k > n:
            return []
        combineHelper([], range(1, n+1), 0, k)
        return rt

    def combine_rec(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

if __name__ == '__main__':
    s = Solution()
    n = 6
    k = 3
    rt1 = s.combine_dp(n, k)
    print rt1

    rt2 = s.combine_rec(n, k)
    print rt2