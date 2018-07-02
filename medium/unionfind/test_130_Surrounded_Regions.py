"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

X X X X
X O O X
X X O X
X O X X

chnage to

X X X X
X X X X
X X X X
X O X X

"""


class UnionFind(object):
    def __init__(self, board, R, C):
        self.father = [-1] * (R * C + 1)
        self.father[R * C] = R * C
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    k = i * C + j
                    self.father[k] = k

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if root_a > root_b:
                self.father[root_b] = root_a
            elif root_a < root_b:
                self.father[root_a] = root_b

    def find(self, root):
        if self.father[root] == root:
            return root
        return self.find(self.father[root])


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        uf = UnionFind(board, R, C)
        dummy = R * C
        for i in range(R):
            if board[i][0] == 'O':
                uf.union(i * C, dummy)
            if board[i][C - 1] == 'O':
                uf.union(i * C + C - 1, dummy)

        for j in range(C):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[R - 1][j] == 'O':
                uf.union((R - 1) * C + j, dummy)

        mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    for dx, dy in mv:
                        n_x, n_y = i + dx, j + dy
                        if 0 <= n_x < R and 0 <= n_y < C and board[n_x][n_y] == 'O':
                            uf.union(i * C + j, n_x * C + n_y)

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and uf.find(i * C + j) != dummy:
                    board[i][j] = 'X'

class Solution(object):
    def solve_dfs(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        unchange = set()
        stk = [(0, 0)] if board[0][0] == 'O' else []
        stk += [(0, j) for j in range(C-1) if board[0][j] == 'O']
        stk += [(i, C-1) for i in range(R-1) if board[i][C-1] == 'O']
        stk += [(R-1, j) for j in range(1, C) if board[R-1][j] == 'O']
        stk += [(i, 0) for i in range(1, R) if board[i][0] == 'O']
        mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stk:
            p = stk.pop()
            if p not in unchange:
                unchange.add(p)
                x, y = p[0], p[1]
                for dx, dy in mv:
                    n_x, n_y = x + dx, y + dy
                    if 0 <= n_x < R and 0 <= n_y < C and board[n_x][n_y] == 'O':
                        stk.append((n_x, n_y))
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and (i, j) not in unchange:
                    board[i][j] = 'X'
        return


