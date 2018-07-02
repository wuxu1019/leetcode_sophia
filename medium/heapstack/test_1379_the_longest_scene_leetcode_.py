
class Solution:
    """
    @param str: The scene string
    @return: Return the length longest scene
    """
    def getLongestScene(self, str):
        # Write your code here
        if not str:
            return 0
        pos = {}
        for n, c in enumerate(str):
            if c not in pos:
                pos[c] = [n, n]
            else:
                pos[c][1] = n
        pos_n = [v for v in pos.values() if v[0] != v[1]]

        if not pos_n:
            return 1

        pos_n.sort()
        print pos_n
        stk = [pos_n[0]]
        for q0, q1 in pos_n[1:]:
            if q0 < stk[-1][1]:
                p0, p1 = stk.pop()
                stk.append([p0, max(q1, p1)])
            else:
                stk.append([q0, q1])

        return max( j - i +1 for i, j in stk)


if __name__ == '__main__':
    s = Solution()
    l = "ufyxjykcohpbuc"
    rt = s.getLongestScene(l)
    print rt